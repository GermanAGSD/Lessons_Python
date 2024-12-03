import httpx
import asyncio
from pydantic import BaseModel
from typing import Optional, List, Union
import json

# Модель для события setvol
class SetVolumeEvent(BaseModel):
    volume: int  # Уровень громкости

# Модель для данных SSE
class ServerSentEvent(BaseModel):
    event: Optional[str] = None  # Тип события
    data: Union[str, dict] = None  # Основное содержимое сообщения

    def parsed_data(self):
        """
        Попытка разобрать data как JSON.
        """
        if self.data:
            try:
                return json.loads(self.data) if isinstance(self.data, str) else self.data
            except json.JSONDecodeError:
                return self.data  # Вернуть как есть, если это не JSON
        return None

async def sse_client():
    url = "http://192.168.1.100:8001/sse/host?param=123"  # URL вашего SSE сервера

    while True:  # Бесконечный цикл для переподключения
        try:
            print("Connecting to SSE endpoint...")
            timeout = httpx.Timeout(10.0, read=60.0)  # Таймаут чтения
            async with httpx.AsyncClient(timeout=timeout) as client:
                async with client.stream("GET", url, headers={"Accept": "text/event-stream"}) as response:
                    print("Connected to SSE endpoint")
                    current_event = ServerSentEvent()  # Текущие данные события

                    async for line in response.aiter_lines():
                        line = line.strip()  # Убираем пробелы в начале и конце строки

                        # Обработка различных частей события
                        if line.startswith("event:"):
                            current_event.event = line[6:].strip()
                        elif line.startswith("data:"):
                            if current_event.data:

                                current_event.data += "\n" + line[5:].strip()  # Добавляем, если это многосрочное "data"
                            else:
                                current_event.data = line[5:].strip()
                        elif line.startswith("id:"):
                            current_event.id = line[3:].strip()
                        elif line == "":
                            # Конец события - обрабатываем текущее событие
                            if current_event.event or current_event.data:
                                if current_event.event == "setvol":
                                    try:
                                        set_vol_data = SetVolumeEvent(**current_event.parsed_data())
                                        print(f"Set Volume Event: Volume = {set_vol_data.volume}")
                                    except (json.JSONDecodeError, TypeError) as e:
                                        print(f"Failed to parse setvol data: {current_event.data}, Error: {e}")
                                # Печатаем тип события и его данные
                                print(f"Event: {current_event.event}, Data: {current_event.parsed_data()}")
                            # Обнуляем текущее событие для следующего
                            current_event = ServerSentEvent()
        except (httpx.ReadTimeout, httpx.ConnectError, httpx.RequestError) as e:
            print(f"Connection lost: {e}. Reconnecting in 5 seconds...")
        except Exception as e:
            print(f"Unexpected error: {e}. Reconnecting in 5 seconds...")
        await asyncio.sleep(5)  # Ожидание перед повторным подключением

if __name__ == "__main__":
    asyncio.run(sse_client())
