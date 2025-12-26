import asyncio
import aiohttp
import json

from mypy.util import json_dumps


class SSEClient:
    """
    Асинхронный SSE-клиент с автопереподключением и JSON-декодированием.
    """

    def __init__(self, url: str, reconnect_delay: float = 3.0):
        self.url = url
        self.reconnect_delay = reconnect_delay
        self._running = False

    async def connect(self):
        """
        Основной цикл подключения к SSE-серверу.
        """
        self._running = True
        print(f"🔌 Connecting to {self.url} ...")

        while self._running:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.url, timeout=None) as resp:
                        if resp.status != 200:
                            print(f"⚠️ Connection failed: HTTP {resp.status}")
                            await asyncio.sleep(self.reconnect_delay)
                            continue

                        print("✅ Connected to SSE stream")
                        async for line in resp.content:
                            line = line.decode("utf-8").strip()
                            if not line or not line.startswith("data:"):
                                continue

                            # убираем 'data:' и пробелы
                            data = line[5:].strip()

                            # пробуем декодировать JSON
                            try:
                                event = json.loads(data)
                            except json.JSONDecodeError:
                                event = data

                            await self.on_message(event)

            except aiohttp.ClientError as e:
                print(f"❌ Connection error: {e}")
                await asyncio.sleep(self.reconnect_delay)
            except asyncio.CancelledError:
                print("🛑 SSE client cancelled")
                break
            except Exception as e:
                print(f"💥 Unexpected error: {e}")
                await asyncio.sleep(self.reconnect_delay)

    async def on_message(self, data):
        """
        Метод, который вызывается при получении события.
        Можно переопределить в наследнике.

        Данные передаются в формате Json
        """
        print(f"📨 Event received: {data}")
        # print(data["volume"])

    async def close(self):
        """Останавливает клиента."""
        self._running = False
        print("🔚 Client stopped")


async def main():
    url = "http://192.168.19.13:8000/sse/host?param=SQL-RK"
    client = SSEClient(url)

    # Запускаем клиента в отдельной задаче
    task = asyncio.create_task(client.connect())

    try:
        # Работаем, пока не нажмут Ctrl+C
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        await client.close()
        task.cancel()
        await asyncio.gather(task, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
