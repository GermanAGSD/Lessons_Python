from typing import List
from fastapi import FastAPI, Request, Depends
from sse_starlette.sse import EventSourceResponse, ServerSentEvent
from sqlalchemy.orm import Session
import asyncio

app = FastAPI()

_streams: List["Stream"] = []  # глобальный список активных подключений


class Stream:
    """Поток событий SSE, основанный на asyncio.Queue"""
    def __init__(self) -> None:
        self._queue: asyncio.Queue[ServerSentEvent] = asyncio.Queue()
        self.client_ip: str | None = None
        self.query_params: str | None = None
        self.active: bool = True  # флаг активности клиента

    def __aiter__(self) -> "Stream":
        return self

    async def __anext__(self) -> ServerSentEvent:
        if not self.active:
            raise StopAsyncIteration
        try:
            return await self._queue.get()
        except asyncio.CancelledError:
            self.active = False
            raise StopAsyncIteration

    async def asend(self, value: ServerSentEvent) -> None:
        """Отправить событие клиенту"""
        if self.active:
            await self._queue.put(value)

    def close(self) -> None:
        """Закрыть поток (например, при отключении клиента)"""
        self.active = False


def regist_host(param: str, db: Session):
    """Заглушка регистрации клиента в БД"""
    print(f"Register host in DB: {param}")


@app.get("/sse/host")
async def sse(
        request: Request,
        db: Session = Depends(get_db),
) -> EventSourceResponse:
    # создаём и регистрируем поток клиента
    stream = Stream()
    stream.client_ip = request.client.host
    stream.query_params = request.query_params.get('param', 'No params')
    _streams.append(stream)

    print(f"✅ Client connected: IP={stream.client_ip}, param={stream.query_params}")

    # регистрация хоста в базе
    regist_host(stream.query_params, db)

    async def event_generator():
        try:
            async for event in stream:
                yield event
        except asyncio.CancelledError:
            # клиент отключился
            stream.close()
            if stream in _streams:
                _streams.remove(stream)
            print(f"❌ Client disconnected: IP={stream.client_ip}, param={stream.query_params}")
            raise
        finally:
            # на всякий случай — гарантированное удаление
            if stream in _streams:
                _streams.remove(stream)
            stream.close()

    return EventSourceResponse(event_generator(), headers={'Cache-Control': 'no-store'})
