import json
import pprint
import sseclient
import urllib3

def with_urllib3(url, headers):
    """Get a streaming response for the given event feed using urllib3."""
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False, headers=headers)

url = "http://192.168.1.100:8001/sse/host?param=123"  # URL вашего SSE сервера
headers = {'Accept': 'text/event-stream'}
response = with_urllib3(url, headers)

# Создаем клиент для работы с SSE, используя потоковый ответ от urllib3
client = sseclient.SSEClient(response)

# Обрабатываем события
for event in client.events():
    try:
        parsed_data = json.loads(event.data)
        pprint.pprint(parsed_data)
    except json.JSONDecodeError:
        print(f"Received non-JSON data: {event.data}")
