from traceback import print_exc

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import uvicorn
from fastapi import Request
from typing import List, Generator
from typing import List, Dict
from lessons_1 import ip_address

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.connection_params: Dict[WebSocket, str] = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.connection_params[websocket] = websocket.url.query
        self.log_active_connections()

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        if websocket in self.connection_params:
            del self.connection_params[websocket]
        self.log_active_connections()

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def send_personal_message(self, websocket: WebSocket, message: str):
        await websocket.send_text(message)

    def log_active_connections(self):
        # Очистка консольного вывода перед отображением новых активных соединений
        print("\033c", end="")
        print(f"Active connections: {len(self.active_connections)}")
        for connection in self.active_connections:
            query_params = self.connection_params.get(connection, "No params")
            print(f"Client connected with query parameters: {query_params}")

manager = ConnectionManager()

ipaddress = []

@app.websocket("/ws/host")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Получение сообщения от клиента
            data = await websocket.receive_text()
            pravila(data)
            query_params = manager.connection_params.get(websocket, "No params")
            print(f"Received from client: {data} - host: {websocket.client.host, websocket.client.port}: param: {query_params}")
            # Отправка ответа всем подключенным клиентам
            await manager.send_personal_message(websocket, f"Server received: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
@app.post("/send_message")
async def send_message(request: Request):
    try:
        body = await request.json()
    except ValueError:
        return {"error": "Invalid JSON"}

    message = body.get("message")
    if message:
        await manager.broadcast(message)
        return {"status": "Message sent"}
    return {"error": "Message not provided"}

def pravila(message):
    if(message == "message"):
        print("Правила работают от Dart client")
    elif(message == "Pravila"):
        print("Правила работают от Python client")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
