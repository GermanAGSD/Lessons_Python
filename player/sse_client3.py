import time
import requests
from sseclient import SSEClient

from ClietnWebSocket import listen

# SSE URL
url = "http://192.168.1.100:8001/sse/host?param=123"

def listen_to_sse():
    while True:
        try:
            print("Подключение к серверу SSE...")
            response = requests.get(url, stream=True, timeout=10)  # Устанавливаем timeout
            client = SSEClient(response)

            for event in client.events():
                match event.event:
                    case 'play':
                        print(f"Event: {event.event}")
                        print(f"Data: {event.data}")
                    case 'setvol':
                        print(f"Event: {event.event}")
                        print(f"Data: {event.data}")
                    case _:
                        print(f"Unknown Event: {event.event}")
                        print(f"Data: {event.data}")
        except (requests.exceptions.RequestException, Exception) as e:
            print(f"Ошибка подключения: {e}")
            print("Повторное подключение через 5 секунд...")
            time.sleep(1)  # Задержка перед переподключением
            listen_to_sse()
if __name__ == "__main__":
    listen_to_sse()