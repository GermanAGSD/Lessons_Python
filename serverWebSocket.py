import asyncio
import websockets


async def hello(websocket):
    name = await websocket.recv()
    print(f'Server rec: {name}')
    greating = f'Helllo {name}'

    await websocket.send(greating)
    print(f'server sent: {greating}')

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()
if __name__ == "__main__":
    asyncio.run(main())