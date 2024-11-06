from traceback import print_exc

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import uvicorn
from fastapi import Request
from typing import List, Generator
from typing import List, Dict, Union
from lessons_1 import ip_address
import json
from pydantic import BaseModel, EmailStr, Field
from pydantic.types import conint
app = FastAPI()

class DataModel(BaseModel):
    cykle: bool
    url: str

class MessageBase(BaseModel):
    message: str
    data: Union[DataModel, str]

class MessageGetInfo(BaseModel):
    message: str
    data: str

class MessageStop(BaseModel):
    message: str
    data: str


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

    async def send_json_message(self, websocket: WebSocket, message: str, data: str):
        payload = json.dumps({"message": message, "data": data})
        await websocket.send_text(payload)

    async def send_json_message2(self, websocket: WebSocket, message: str, data: Union[DataModel, str]):
    # Если data является экземпляром DataModel, преобразуем его в словарь
        if isinstance(data, DataModel):
            data = data.dict()
        payload = json.dumps({"message": message, "data": data})
        await websocket.send_text(payload)

manager = ConnectionManager()

ipaddress = []

@app.websocket("/ws/host")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Получение сообщения от клиента
            data = await websocket.receive_text()

            query_params = manager.connection_params.get(websocket, "No params")
            print(f"Received from client: {data} - host: {websocket.client.host, websocket.client.port}: param: {query_params}")
            # Отправка ответа всем подключенным клиентам
            await manager.send_personal_message(websocket, f"Server received: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)




@app.post("/getinfo")
async def get_info(msg: MessageGetInfo):
    if msg.message and msg.data:
        for connection in manager.active_connections:
            await manager.send_json_message(connection, msg.message, msg.data)
        return {"status": "Message sent"}
    return {"error": "Message or data not provided"}

@app.post("/play")
async def play_funct(msg: MessageBase):
    if msg.message and msg.data:
        for connection in manager.active_connections:
            await manager.send_json_message2(connection, msg.message, msg.data)
        return {"status": "Message sent"}
    return {"error": "Message or data not provided"}

@app.post("/stop")
async def stop_funct(msg: MessageStop):
    if msg.message and msg.data:
        for connection in manager.active_connections:
            await manager.send_json_message(connection, msg.message, msg.data)
        return {"status": "Message sent"}
    return {"error": "Message or data not provided"}

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.100", port=8001)
