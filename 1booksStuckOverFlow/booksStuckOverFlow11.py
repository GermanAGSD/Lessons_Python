import asyncio
import aiohttp


class EchoWebsocket:
    def __init__(self):
        self.websocket = None
        self.session = None

    async def connect(self):
        self.session = aiohttp.ClientSession()
        self.websocket = await self.session.ws_connect("wss://echo.websocket.org")
        print("Connected to WebSocket")

    async def send(self, message):
        if self.websocket is None:
            raise ConnectionError("WebSocket connection is not established.")
        await self.websocket.send_str(message)
        print(f"Sent: {message}")

    async def receive(self):
        if self.websocket is None:
            raise ConnectionError("WebSocket connection is not established.")
        result = await self.websocket.receive()
        return result.data

    async def close(self):
        if self.websocket:
            await self.websocket.close()
        if self.session:
            await self.session.close()


async def main():
    echo = EchoWebsocket()
    try:
        await echo.connect()
        await echo.send("Hello")
        response = await echo.receive()
        print(f"Received: {response}")
    finally:
        # Закрытие соединения в любом случае
        await echo.close()


if __name__ == "__main__":
    asyncio.run(main())

