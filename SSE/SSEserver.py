from fastapi import FastAPI, Request, Depends, HTTPException
from sse_starlette.sse import EventSourceResponse, ServerSentEvent
from typing import List, Union, Optional
import uvicorn
from pydantic import BaseModel, Field
from starlette import status
from SSE.Models import Models
from SSE.Database.DataBaseSqlAlchemy import engine, get_db
from sqlalchemy.orm import Session
import asyncio
import json
from httpx import AsyncClient
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешённые источники (можно указать Django, localhost и т.д.)
origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://192.168.19.13:8000",  # если Django тоже крутится на этом IP
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # или ["*"] для всех
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Разрешённые источники (можно указать Django, localhost и т.д.)
origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://192.168.19.13:8000",  # если Django тоже крутится на этом IP
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # или ["*"] для всех
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ParamsOut(BaseModel):
    params: str

class CommentsOut(BaseModel):
    id: int
    post: str
    likescount: int

    class Config:
        orm_mode = True  # Позволяет Pydantic работать с объектами SQLAlchemy

class Address(BaseModel):
    street: str = Field(..., description="The street name of the company address")
    number: str = Field(..., description="The building number")
    zipcode: str = Field(..., description="The ZIP code of the location")

class Company(BaseModel):
    companyName: str = Field(..., alias="companyNmae", description="The name of the company")
    activity: str = Field(..., description="The primary activity of the company")
    address: Address = Field(..., description="The company's address details")
    yearsOfEstam: int = Field(..., description="The year the company was established")
# 1 - true
class GetHost(BaseModel):
    id: int
    params: str
    name: str
    region: str

class StopModel(BaseModel):
    stop: int

class PlayUrls(BaseModel):
    url: str

class PlayModel(BaseModel):
    urls: List[PlayUrls]
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

class UserCreate(BaseModel):
    login: str
    password: str

class UserLogin(BaseModel):
    login: str
    password: str
# Модель для данных, которые будут приходить от клиента через POST запрос
# class ClientDataModel(BaseModel):
#     param: str
#     message: str
#     data: Union[str, dict]

class ClientDataModel(BaseModel):
    duration: float
    position: float
    volume: Optional[float] = None
    status: Optional[str] = None
# Определяем модель данных для вебхука
class WebhookData(BaseModel):
    event: str
    payload: dict


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

# class Stream:
#     def __init__(self) -> None:
#         self._queue = asyncio.Queue[ServerSentEvent]()
#
#     def __aiter__(self) -> "Stream":
#         return self
#
#     async def __anext__(self) -> ServerSentEvent:
#         return await self._queue.get()
#
#     async def asend(self, value: ServerSentEvent) -> None:
#         await self._queue.put(value)
#
# _streams: List[Stream] = []


@app.get("/sse/host")
async def sse(request: Request, db: Session = Depends(get_db)) -> EventSourceResponse:
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


@app.get("/comment", response_model=List[CommentsOut])
def getComment(db: Session = Depends(get_db)):
    result = db.query(Models.Comment).all()
    return result
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


# @app.get("/sse/host")
# async def sse(request: Request, db: Session = Depends(get_db),stream: Stream = Depends()) -> EventSourceResponse:
#     stream = Stream()
#     query_params = request.query_params.get('param', 'No params')
#     stream.client_ip = request.client.host
#     stream.query_params = query_params
#     _streams.append(stream)
#     print(f"Client connected: IP address: {stream.client_ip}, Query params: {stream.query_params}")
#
#     # webhook to FrontEnd
#     # Отправляем POST-запрос о подключении клиента
#     # await post_to_server(
#     #     "http://localhost:8000/sse/client-connected",
#     #     {"client_ip": stream.client_ip, "query_params": stream.query_params},
#     # )
#
#     # Проверка и регистрация хоста в базе данных
#     regist_host(stream.query_params, db)
#     async def event_generator():
#         try:
#             async for event in stream:
#                 yield event
#         except asyncio.CancelledError:
#             _streams.remove(stream)
#             print(f"Client disconnected: IP address: {stream.client_ip}, Query params: {stream.query_params}")
#             raise
#
#     return EventSourceResponse(event_generator(), headers={'Cache-Control': 'no-store'})
#     try:
#         query_params = request.query_params.get('param', 'No params')
#         stream.client_ip = request.client.host
#         stream.query_params = query_params
#         _streams.append(stream)
#         print(f"Client connected: IP address: {stream.client_ip}, Query params: {stream.query_params}")
#         return EventSourceResponse(stream, headers={'Cache-Control': 'no-store'})
#     except asyncio.CancelledError:
#         _streams.remove(stream)
#         print(f"Client disconnected: IP address: {stream.client_ip}, Query params: {stream.query_params}")
#         raise
#     query_params = request.query_params.get('param', 'No params')
#     stream.client_ip = request.client.host
#     stream.query_params = query_params
#     _streams.append(stream)
#     return EventSourceResponse(stream, headers={'Cache-Control': 'no-store'})

# Data to webHook
async def post_to_server(url, data):
    async with AsyncClient() as client:
        response = await client.post(url, json=data)
        print(f"POST response: {response.status_code}, {response.text}")


@app.post("/webhook")
async def webhook_handler(data: WebhookData):
    try:
        print(f"Received event: {data.event}")
        print(f"Payload: {data.payload}")
        # Обработка данных, например, запись в лог или выполнение действия
        return {"status": "success", "message": "Webhook processed successfully"}
    except Exception as e:
        print(f"Error processing webhook: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post("/message", status_code=status.HTTP_200_OK)
async def send_message(host: str,data: str, event: str, stream: Stream = Depends()) -> None:
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=data, event=event)
            )


@app.post("/setvol", status_code=status.HTTP_200_OK)
async def setvol(host: str, data: SetvolModel, stream: Stream = Depends()) -> None:
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=data.json(), event="setvol")
            )

@app.post("/play", status_code=status.HTTP_200_OK)
async def playVideo(host: str, play: PlayModel, stream: Stream = Depends()) -> None:
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=play.json(), event="play")
            )

@app.post("/pause", status_code=status.HTTP_200_OK)
async def pauseVideo(host: str, stream: Stream = Depends()) -> None:
    jsstr = {
        "pause": 0
    }
    json.dumps(jsstr)
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=jsstr, event="pause")
            )

@app.post("/replay", status_code=status.HTTP_200_OK)
async def replayVideo(host: str, stream: Stream = Depends()) -> None:
    jsstr = {
        "replay": 0
    }
    json.dumps(jsstr)
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=jsstr, event="replay")
            )

@app.post("/getinfo", status_code=status.HTTP_200_OK)
async def getinfoVideo(host: str, stream: Stream = Depends()) -> None:
    jsstr = {
        "getinfo": 0
    }
    json.dumps(jsstr)
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=jsstr, event="getinfo")
            )

@app.post("/company", status_code=status.HTTP_200_OK)
async def company(host: str, cmp: Company, stream: Stream = Depends()) -> None:
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(data=cmp.json(), event="company")
            )

@app.post("/stop", status_code=status.HTTP_200_OK)
async def stopVideo(host: str, stop: StopModel, stream: Stream = Depends()) -> None:
    jsstr = {
        "stop": 0
    }
    js = json.dumps(jsstr)
    for stream in _streams:
        if stream.query_params == host:
            await stream.asend(
                ServerSentEvent(event="stop", data=js)
            )

@app.get("/gethosts", response_model=List[ParamsOut])
def get_hosts(db: Session = Depends(get_db)):
    result = db.query(Models.Hosts).all()
    return result


# Асинхронная функция для выполнения SQL-запроса
# Асинхронная функция для получения хостов
# Асинхронная функция для получения хостов
# async def fetch_hosts(dbs: AsyncSession):
#     result = await dbs.execute(select(Models.Hosts))
#     hosts = result.scalars().all()
#     return hosts
#
# # Синхронная функция, которая может выполняться в пуле потоков
# def process_host_data_sync(data):
#     # Представьте, что здесь сложная обработка данных
#     for host in data:
#         process_data = [f"Processed: {host.params} - {host.name} - {host.region}"]
#     # processed_data = [f"Processed: {host.params} - {host.name} - {host.region}" for host in data]
#
#     return data
#
# @app.get("/get_hosts_async")
# async def get_hosts_async(dbs: AsyncSession = Depends(get_db_async)):
#     try:
#         # Попытка выполнения запроса
#         hosts = await fetch_hosts(dbs)
#     except DBAPIError as e:
#         # Обработка потери соединения
#         print(f"Database error occurred: {e}")
#         # Можете попробовать переподключиться или вернуть сообщение об ошибке
#         return {"error": "Database connection issue, please try again later."}
#
#     # Логика обработки данных, если соединение не было потеряно
#     loop = asyncio.get_event_loop()
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         processed_hosts = await loop.run_in_executor(executor, process_host_data_sync, hosts)
#
#     return {"hosts": processed_hosts}
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
    print(f"Received data from client {query_params} - duration: {client_data.duration}, position: {client_data.position}, volume: {client_data.volume}, status: {client_data.status}")

    return {"status": "Data received successfully"}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(bdpassword, inputpassword) -> bool:
    hashpass = get_password_hash(inputpassword)
    return hashpass == bdpassword

def get_password_hash(password):
    return pwd_context.hash(password)
# JWT settings
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY = "my_secret_key"  # Make sure this is kept safe and not exposed
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 90


# Создание токена с учётом временных зон
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Эндпоинт для регистрации пользователя
@app.post("/register")
def register_user(usercreate: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(usercreate.password)
    user = Models.Users(name=usercreate.login, password=hashed_password)
    db.add(user)
    # db.commit()
    # db.refresh(user)
    # new_host = Models.Users(params=host.params)
    # db.add(user)
    # db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except:
        db.rollback()
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    return {"message": "Пользователь успешно зарегистрирован"}
# Эндпоинт для логина пользователя
# Маршрут для логина пользователя
@app.post("/login/")
async def login(userlog: UserCreate, db: Session = Depends(get_db)):
    # Ищем пользователя по логину
    user = db.query(Models.Users).filter(Models.Users.name == userlog.login).first()
    # print(user)
    # Проверяем, существует ли пользователь
    if not user:
        raise HTTPException(status_code=400, detail="Invalid login or password")

    # # Проверяем пароль с использованием безопасного сравнения хэшей
    if not user.password != get_password_hash(userlog.password):
        # print(userlog.password)
        # print(user.password)
        raise HTTPException(status_code=400, detail="Invalid login or password")

    access_token = create_access_token(data={"user_id": user.id})

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.19.13", port=8000)