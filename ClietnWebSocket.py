import asyncio
import websockets

counter = 0
async def listen():
    uri = "ws://localhost:8001/ws/host?param=123"
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                print("Connected to WebSocket server")
                while True:
                    message = await websocket.recv()
                    await pravila(message, websocket)
                    print(f"Received message: {message}")
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed, retrying in 5 seconds...")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"Unexpected error: {e}, retrying in 5 seconds...")
            await asyncio.sleep(5)

async def pravila(message, websocket):
    counter + 1
    if message == "hello world":
        print("Hello world правила работают")
        # Отправка ответа обратно на сервер через WebSocket
        await send_response(websocket, f"Pravila")

async def send_response(websocket, response_message):
    try:
        await websocket.send(response_message)
        print(f"Sent response: {response_message}")
    except Exception as e:
        print(f"Failed to send response: {e}")

if __name__ == "__main__":
    asyncio.run(listen())
