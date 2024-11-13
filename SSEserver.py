from traceback import print_exc
from fastapi import FastAPI, Request, Depends
from sse_starlette.sse import EventSourceResponse, ServerSentEvent
from typing import List, Dict, Union, Generator
import uvicorn
import json
import asyncio
from pydantic import BaseModel
from pydantic.types import conint
from lessons_1 import ip_address
from starlette import status
import Models
from DataBaseSqlAlchemy import engine, get_db
from sqlalchemy.orm import Session
Models.Base.metadata.create_all(bind=engine)
app = FastAPI()
# 1 - true
class StopModel(BaseModel):
    stop: int

class PlayModel(BaseModel):
    urls: str
# Модель для представления массива видео

class VideoListModel(BaseModel):
    urls: List[PlayModel]

class MessagePlay(BaseModel):
    event: str
    data: Union[PlayModel, str]


class SetvolModel(BaseModel):
    volume: float

class MessageSetvol(BaseModel):
    event: str
    data: Union[SetvolModel, str]

class MessageGetInfo(BaseModel):
    message: str
    data: str

class MessageStop(BaseModel):
    message: str
    data: str

class HostCreate(BaseModel):
    params: str

# Модель для данных, которые будут приходить от клиента через POST запрос
class ClientDataModel(BaseModel):
    param: str
    message: str
    data: Union[str, dict]

class Stream:
    def __init__(self) -> None:
        self._queue = asyncio.Queue[ServerSentEvent]()

    def __aiter__(self) -> "Stream":
        return self

    async def __anext__(self) -> ServerSentEvent:
        return await self._queue.get()

    async def asend(self, value: ServerSentEvent) -> None:
        await self._queue.put(value)

_streams: List[Stream] = []


# Добавим функцию для регистрации новых устройств в базе данных
def regist_host(parammetr, db: Session):
    result = db.query(Models.Hosts).filter(Models.Hosts.params == parammetr).first()
    if result:
        print(f"Device with param {parammetr} is already registered.")
    else:
        new_host = Models.Hosts(params=parammetr)
        db.add(new_host)
        db.commit()
        db.refresh(new_host)
        print(f"New device registered with param {parammetr}.")


@app.get("/sse/host")
async def sse(request: Request, db: Session = Depends(get_db),stream: Stream = Depends()) -> EventSourceResponse:
    stream = Stream()
    query_params = request.query_params.get('param', 'No params')
    stream.client_ip = request.client.host
    stream.query_params = query_params
    _streams.append(stream)
    print(f"Client connected: IP address: {stream.client_ip}, Query params: {stream.query_params}")
    # Проверка и регистрация хоста в базе данных
    regist_host(stream.query_params, db)
    async def event_generator():
        try:
            async for event in stream:
                yield event
        except asyncio.CancelledError:
            _streams.remove(stream)
            print(f"Client disconnected: IP address: {stream.client_ip}, Query params: {stream.query_params}")
            raise

    return EventSourceResponse(event_generator(), headers={'Cache-Control': 'no-store'})
    try:
        query_params = request.query_params.get('param', 'No params')
        stream.client_ip = request.client.host
        stream.query_params = query_params
        _streams.append(stream)
        print(f"Client connected: IP address: {stream.client_ip}, Query params: {stream.query_params}")
        return EventSourceResponse(stream, headers={'Cache-Control': 'no-store'})
    except asyncio.CancelledError:
        _streams.remove(stream)
        print(f"Client disconnected: IP address: {stream.client_ip}, Query params: {stream.query_params}")
        raise
    query_params = request.query_params.get('param', 'No params')
    stream.client_ip = request.client.host
    stream.query_params = query_params
    _streams.append(stream)
    return EventSourceResponse(stream, headers={'Cache-Control': 'no-store'})

@app.post("/message", status_code=status.HTTP_200_OK)
async def send_message(data: str, event: str, stream: Stream = Depends()) -> None:
    for stream in _streams:
        await stream.asend(
            ServerSentEvent(data=data, event=event)
        )
# @app.post("/setvol", status_code=status.HTTP_201_CREATED)
# async def setvol(data: float, event: str, stream: Stream = Depends()) -> None:
#     for stream in _streams:
#         await stream.asend(
#             ServerSentEvent(data=data, event=event)
#         )

@app.post("/setvol", status_code=status.HTTP_200_OK)
async def setvol(host: str, data: SetvolModel, event: str, stream: Stream = Depends()) -> None:
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=data.volume, event=event)
            )

@app.post("/play", status_code=status.HTTP_200_OK)
async def playVideo(play: PlayModel, event: str, stream: Stream = Depends()) -> None:
    for stream in _streams:
        await stream.asend(
            ServerSentEvent(data=play.urls, event=event)
        )

@app.post("/stop", status_code=status.HTTP_200_OK)
async def stopVideo(stop: StopModel, stream: Stream = Depends()) -> None:
    for stream in _streams:
        await stream.asend(
            ServerSentEvent(data=stop.stop, event="stop")
        )
#
@app.get("/gethosts", status_code=status.HTTP_200_OK)
def get_hosts(db: Session = Depends(get_db)):
    result = db.query(Models.Hosts).all()
    return result

@app.post("/hosts", status_code=status.HTTP_201_CREATED)
def create_host(host: HostCreate, db: Session = Depends(get_db)):
    new_host = Models.Hosts(params=host.params)
    db.add(new_host)
    db.commit()
    db.refresh(new_host)
    new_host = Models.Hosts(params=host.params)
    db.add(new_host)
    return {"id": new_host.id, "params": new_host.params, "created_at": new_host.created_at}

# Новый эндпоинт для получения данных от клиента с использованием POST
@app.post("/send_data", status_code=status.HTTP_200_OK)
async def receive_data(data: ClientDataModel):
    """
    Получение данных от клиента через POST запрос и вывод их в консоль.
    """
    # Выводим полученные данные в консоль
    print(f"Received data from client: Param={data.param}, Message={data.message}, Data={data.data}")

    # Здесь можно добавить логику для обработки данных,
    # например, сохранение в базе данных или отправка другим клиентам по желанию.

    return {"status": "Data received successfully"}




@app.get("/active_hosts")
async def print_active_hosts():
    print("c", end="")
    print(f"Active connections: {len(_streams)}")
    query_params_list = []
    for idx, stream in enumerate(_streams, start=1):
        client_ip = getattr(stream, 'client_ip', 'Unknown')
        print(f"Host {idx}: IP address: {client_ip}, Query params: {getattr(stream, 'query_params', 'No params')}")
        query_params = getattr(stream, 'query_params', 'No params')
        query_params_list.append(query_params)
    return {"status": query_params_list}


# Новый эндпоинт для получения данных от клиента с использованием POST
class ClientDataModel(BaseModel):
    duration: int
    position: int
    volume: int
    status: str

@app.post("/receive_data/host", status_code=status.HTTP_200_OK)
async def receive_data(request: Request):
    """
    Получение необработанных данных от клиента через POST запрос и вывод их в консоль.
    """
    # Получаем JSON-данные из тела запроса
    query_params = request.query_params.get('param', 'No param provided')
    data = await request.json()

    # Парсинг JSON-данных в модель Pydantic
    try:
        client_data = ClientDataModel(**data)
    except ValueError as e:
        return {"error": f"Invalid data: {e}"}

    # Выводим полученные данные и их атрибуты в консоль
    print(f"Received data from client  - duration: {client_data.duration}, position: {client_data.position}, volume: {client_data.volume}, status: {client_data.status}")

    return {"status": "Data received successfully"}
if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.100", port=8001)
