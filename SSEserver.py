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
app = FastAPI()

class DataModel(BaseModel):
    urls: str

class MessageBase(BaseModel):
    event: str
    data: Union[DataModel, str]

class MessageGetInfo(BaseModel):
    message: str
    data: str

class MessageStop(BaseModel):
    message: str
    data: str

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

@app.get("/sse/host")

async def sse(request: Request, stream: Stream = Depends()) -> EventSourceResponse:
    stream = Stream()
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

@app.post("/message", status_code=status.HTTP_201_CREATED)
async def send_message(message: MessageBase, stream: Stream = Depends()) -> None:
    for stream in _streams:
        await stream.asend(
            ServerSentEvent(data=message.data, event=message.event)
        )
@app.post("/setvol", status_code=status.HTTP_201_CREATED)
async def setvol(data: str, event: str, stream: Stream = Depends()) -> None:
    for stream in _streams:
        await stream.asend(
            ServerSentEvent(data=data, event=event)
        )
@app.get("/active_hosts")
async def print_active_hosts():
    print("c", end="")
    print(f"Active connections: {len(_streams)}")
    for idx, stream in enumerate(_streams, start=1):
        client_ip = getattr(stream, 'client_ip', 'Unknown')
        print(f"Host {idx}: IP address: {client_ip}, Query params: {getattr(stream, 'query_params', 'No params')}")
    return {"status": "Hosts printed in console"}

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.100", port=8001)
