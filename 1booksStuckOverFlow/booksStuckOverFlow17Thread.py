# Многопоточность

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue, Empty

def echo_client(q):
    """Обработчик клиентов (worker)"""
    while True:
        try:
            client_sock, client_addr = q.get(timeout=1)  # Ожидание клиента с таймаутом
        except Empty:
            continue  # Очередь пуста, продолжаем ожидание

        print(f"Обслуживание клиента: {client_addr}")

        try:
            while True:
                data = client_sock.recv(1024)
                if not data:
                    break
                client_sock.sendall(data)  # Отправляем обратно (echo)
        except Exception as e:
            print(f"Ошибка обработки клиента {client_addr}: {e}")
        finally:
            client_sock.close()
            q.task_done()

def echo_server(addr, nworkers):
    """Сервер с пулом потоков"""
    print('Echo server running at', addr)

    # Создание очереди клиентов
    q = Queue()

    # Запуск клиентских обработчиков (workers)
    for _ in range(nworkers):
        t = Thread(target=echo_client, args=(q,))
        t.daemon = True
        t.start()

    # Запуск сервера
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)

    try:
        while True:
            client_sock, client_addr = sock.accept()
            q.put((client_sock, client_addr))  # Отправка клиента в очередь
    except KeyboardInterrupt:
        print("\nОстановка сервера...")
    finally:
        sock.close()

# Запуск сервера на порту 15000 с 5 worker'ами
echo_server(("127.0.0.1", 15000), 5)
