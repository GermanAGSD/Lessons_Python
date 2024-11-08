from traceback import print_exc
from fastapi import FastAPI, Request, Depends
from sse_starlette.sse import EventSourceResponse, ServerSentEvent
from typing import List, Dict, Union, Generator
import uvicorn
import json
import asyncio
from pydantic import BaseModel
from pydantic.types import conint
from starlette import status
app = FastAPI()

# 1 - true
class StopModel(BaseModel):
    stop: int

class PlayModel(BaseModel):
    urls: str

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

class Stream:
    def __init__(self) -> None:
        self._queue = None

    async def initialize_queue(self):
        # Создаем очередь в асинхронной функции, где есть цикл событий
        self._queue = asyncio.Queue[ServerSentEvent]()

    def __aiter__(self) -> "Stream":
        return self

    async def __anext__(self) -> ServerSentEvent:
        if self._queue is None:
            raise RuntimeError("Queue not initialized. Call initialize_queue() first.")
        return await self._queue.get()

    async def asend(self, value: ServerSentEvent) -> None:
        if self._queue is None:
            raise RuntimeError("Queue not initialized. Call initialize_queue() first.")
        await self._queue.put(value)

_streams: List[Stream] = []

@app.get("/sse/host")
async def sse(request: Request) -> EventSourceResponse:
    stream = Stream()
    await stream.initialize_queue()
    query_params = request.query_params.get('param', 'No params')
    stream.client_ip = request.client.host
    stream.query_params = query_params
    _streams.append(stream)
    print(f"Client connected: IP address: {stream.client_ip}, Query params: {stream.query_params}")

    async def event_generator():
        try:
            async for event in stream:
                yield event
        except asyncio.CancelledError:
            _streams.remove(stream)
            print(f"Client disconnected: IP address: {stream.client_ip}, Query params: {stream.query_params}")
            raise

    return EventSourceResponse(event_generator(), headers={'Cache-Control': 'no-store'})

@app.post("/message", status_code=status.HTTP_201_CREATED)
async def send_message(host: str, data: str, event: str) -> None:
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=data, event=event)
            )

@app.post("/setvol", status_code=status.HTTP_201_CREATED)
async def setvol(host: str, data: SetvolModel, event: str) -> None:
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=str(data.volume), event=event)
            )

@app.post("/play", status_code=status.HTTP_201_CREATED)
async def playVideo(host: str, play: PlayModel, event: str) -> None:
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=play.urls, event=event)
            )

@app.post("/stop", status_code=status.HTTP_201_CREATED)
async def stopVideo(host: str, stop: StopModel) -> None:
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=str(stop.stop), event="stop")
            )

@app.get("/active_hosts")
async def print_active_hosts():
    print("\033c", end="")
    print(f"Active connections: {len(_streams)}")
    for idx, stream in enumerate(_streams, start=1):
        client_ip = getattr(stream, 'client_ip', 'Unknown')
        print(f"Host {idx}: IP address: {client_ip}, Query params: {getattr(stream, 'query_params', 'No params')}")
    return {"status": "Hosts printed in console"}

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.220.119", port=8001)
