# from xmlrpc.client import DateTime
#
# from pydantic import BaseModel, EmailStr, Field
# from datetime import datetime
# from typing import Optional
#
# from pydantic.types import conint
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# import json
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# from fastapi import FastAPI, Request
# from fastapi.responses import StreamingResponse
# import asyncio
#
# from lessons_1 import result
#
# app = FastAPI()
#
# origins = ["*"]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# while True:
#     try:
#         conn = psycopg2.connect(host='172.30.30.19', port='5431', database='fastapi', user='postgres',
#                                 password='password123', cursor_factory=RealDictCursor)
#         # conn = psycopg2.connect(host='172.30.30.8', port='5432', database='livequeue', user='livequeue',
#         #                         password='a~Lvn@Ja#EV~Xu$z', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
#
# @app.get("/sse")
# async def sse_endpoint(request: Request):
#     client_ip = request.client.host
#     print(f"Client {client_ip} connected to SSE")
#     async def event_generator():
#         event_id = 0
#         while True:
#             # Проверяем, если клиент отменил запрос
#             if await request.is_disconnected():
#                 print(f"Client {client_ip} disconnected from SSE")
#                 break
#             # Генерация данных для отправки
#             event = {
#                 "id": event_id,
#                 "event": "event",
#                 "data": {
#                     "message": "Hello, this is an SSE message!"
#                 }
#             }
#             yield f"id: {event['id']}\nevent: {event['event']}\ndata: {json.dumps(event['data'])}\n\n"
#             event_id += 1
#             await asyncio.sleep(1)
#
#     return StreamingResponse(event_generator(), media_type="text/event-stream")
#
#
# class SchemaHost(BaseModel):
#     id: int
#     ipadress: str
#     port: int
#     username: str
#     password: str
#     created: datetime
#
# @app.get("/hosts")
# def get_network_host():
#     # Фильтрация записей по значению hosttype (например, "Network")
#     cursor.execute("""
#         SELECT hosts.*
#         FROM hosts
#         """)
#     type = cursor.fetchall()
#
#     return type

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8001)