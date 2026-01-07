import socket
import threading
import re
import psycopg2
from ldap3 import Server, Connection, ALL, SUBTREE
from cachetools import TTLCache
import time
import logging

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)
logger = logging.getLogger("icap-server")

# ======= КОНФИГУРАЦИЯ =======
LDAP_HOST = "172.30.30.3"
LDAP_PORT = 389
BASE_DN = "DC=bull,DC=local"
SERVICE_BIND_DN = "CN=my-service,CN=Users,DC=bull,DC=local"
SERVICE_PASSWORD = ""

# PostgreSQL
PG_HOST = '172.30.30.8'
PG_PORT = 5432
PG_USER = ''
PG_PASSWORD = ''
PG_DB = ''

# Порт ICAP-сервера
ICAP_PORT = 1344
ICAP_HOST = '0.0.0.0'

# Кэширование
USER_OU_CACHE = TTLCache(maxsize=1000, ttl=600)
OU_PROXY_CACHE = TTLCache(maxsize=100, ttl=600)
user_cache_lock = threading.RLock()
ou_cache_lock = threading.RLock()

def log_raw_data(prefix, data):
    logger.info(f"===== {prefix} =====\n{data.decode('utf-8', errors='replace')}")

def extract_username(full_username):
    if '\\' in full_username:
        return full_username.split('\\')[-1]
    elif '@' in full_username:
        return full_username.split('@')[0]
    return full_username

def get_user_ou(username):
    try:
        server = Server(LDAP_HOST, port=LDAP_PORT, get_info=ALL)
        conn = Connection(server, user=SERVICE_BIND_DN, password=SERVICE_PASSWORD, auto_bind=True)
        search_filter = f"(sAMAccountName={username})"
        conn.search(BASE_DN, search_filter, search_scope=SUBTREE, attributes=["distinguishedName"])

        if not conn.entries:
            logger.warning(f"\u274c Пользователь не найден: {username}")
            return None

        dn = conn.entries[0].distinguishedName.value
        for part in dn.split(','):
            if part.startswith("OU="):
                return part.replace("OU=", "")
        return None
    except Exception as e:
        logger.error(f"\u274c Ошибка: {e}")
        return None

def get_proxy_address(ou):
    with ou_cache_lock:
        if ou in OU_PROXY_CACHE:
            return OU_PROXY_CACHE[ou]
        try:
            conn = psycopg2.connect(
                host=PG_HOST,
                port=PG_PORT,
                user=PG_USER,
                password=PG_PASSWORD,
                database=PG_DB
            )
            cursor = conn.cursor()
            cursor.execute("SELECT remote_ips FROM restaurants WHERE ldap_ou = %s", (ou,))
            result = cursor.fetchone()
            if not result or not result[0]:
                logger.warning(f"Для OU '{ou}' не найдены IP-адреса в базе")
                return None
            first_ip = result[0].split(',')[0].strip()
            ip_parts = first_ip.split('.')
            if len(ip_parts) != 4:
                logger.warning(f"Некорректный формат IP: {first_ip}")
                return None
            proxy_ip = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.1:3128"
            logger.info(f"Для OU '{ou}' преобразован IP: {first_ip} -> {proxy_ip}")
            OU_PROXY_CACHE[ou] = proxy_ip
            return proxy_ip
        except Exception as e:
            logger.error(f"Ошибка подключения к PostgreSQL: {str(e)}")
            return None
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'conn' in locals() and conn:
                conn.close()

def parse_icap_request(data):
    headers = {}
    lines = data.decode('utf-8').split('\r\n')

    if not lines:
        return None, None, None

    request_line = lines[0]
    method = request_line.split()[0] if ' ' in request_line else None

    for line in lines[1:]:
        if not line.strip():
            break
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip().lower()] = value.strip()

    username = None
    if 'x-client-username' in headers:
        username = extract_username(headers['x-client-username'])

    http_start = data.find(b'\r\n\r\n') + 4
    http_data = data[http_start:] if http_start > 3 else b''

    return method, username, http_data

def modify_http_request(http_data, username):
    if not http_data:
        return http_data

    try:
        http_text = http_data.decode('utf-8')
    except UnicodeDecodeError:
        http_text = http_data.decode('latin-1')

    if not username:
        return http_data

    ou = get_user_ou(username)
    if not ou:
        return http_data

    proxy_address = get_proxy_address(ou)
    if not proxy_address:
        return http_data

    logger.info(f"Добавлены заголовки: X-Authenticated-User={username}, X-Proxy-Address={proxy_address}")

    header_end = http_text.find('\r\n\r\n')
    if header_end == -1:
        return http_data

    headers_part = http_text[:header_end]
    body = http_text[header_end:]
    new_headers = (
        f"{headers_part}\r\n"
        f"X-Authenticated-User: {username}\r\n"
        f"X-Proxy-Address: {proxy_address}"
    )
    return (new_headers + body).encode('utf-8')

def handle_options():
    response = [
        "ICAP/1.0 200 OK",
        "Methods: REQMOD",
        "Service: Simple ICAP Server",
        "Transfer-Preview: *",
        "Allow: 204",
        "Encapsulated: null-body=0",
        "",
        ""
    ]
    return "\r\n".join(response).encode('utf-8')

def handle_reqmod(data, username):
    http_data = data[data.find(b'\r\n\r\n') + 4:]
    modified_http = modify_http_request(http_data, username)

    if modified_http == http_data:
        response = [
            "ICAP/1.0 204 No Content",
            "Encapsulated: null-body=0",
            "",
            ""
        ]
        return "\r\n".join(response).encode('utf-8')
    else:
        logger.info("\U0001f4e6 Модифицированный HTTP-запрос:")
        logger.info(modified_http.decode('utf-8', errors='replace'))
        response = [
            "ICAP/1.0 200 OK",
            f"Encapsulated: req-hdr=0, null-body={len(modified_http)}",
            "",
            ""
        ]
        return "\r\n".join(response).encode('utf-8') + modified_http

def handle_client(conn):
    try:
        data = conn.recv(65536)
        if not data:
            return

        logger.info("=== Получен ICAP-запрос ===")
        log_raw_data("REQUEST", data)

        method, username, http_data = parse_icap_request(data)

        if method == "OPTIONS":
            response = handle_options()
        elif method == "REQMOD":
            response = handle_reqmod(data, username)
        else:
            response = "ICAP/1.0 405 Method Not Allowed\r\n\r\n".encode('utf-8')

        log_raw_data("RESPONSE", response)
        conn.sendall(response)

    except Exception as e:
        logger.error(f"Ошибка обработки запроса: {str(e)}")
    finally:
        conn.close()

def run_server():
    logger.info("="*50)
    logger.info(f"Запуск ICAP-сервера на {ICAP_HOST}:{ICAP_PORT}")
    logger.info(f"AD сервер: {LDAP_HOST}")
    logger.info(f"PG сервер: {PG_HOST}:{PG_PORT}")
    logger.info(f"База данных: {PG_DB}")
    logger.info("="*50)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((ICAP_HOST, ICAP_PORT))
    server_socket.listen(5)

    try:
        while True:
            conn, addr = server_socket.accept()
            logger.info(f"Подключение от {addr[0]}:{addr[1]}")
            client_thread = threading.Thread(target=handle_client, args=(conn,))
            client_thread.daemon = True
            client_thread.start()
    except KeyboardInterrupt:
        logger.info("Остановка сервера...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    run_server()