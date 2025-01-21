from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List
import uvicorn
# Модель Pydantic для валидации данных
class Item(BaseModel):
    name: str
    description: str
    price: float

# Модель для ответа с MongoDB ObjectId
class ItemResponse(Item):
    id: str

# Конфигурация приложения FastAPI
app = FastAPI()

# Подключение к MongoDB
MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client.test_database  # Используем базу данных test_database
collection = db.items      # Коллекция items

# Помощник для преобразования ObjectId в строку
def item_helper(item) -> dict:
    item["id"] = str(item["_id"])
    del item["_id"]
    return item

# GET запрос: Получение всех элементов
@app.get("/items", response_model=List[ItemResponse])
async def get_items():
    items = []
    async for item in collection.find():
        items.append(item_helper(item))
    return items

# GET запрос: Получение элемента по ID
@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_helper(item)

# POST запрос: Добавление нового элемента
@app.post("/items", response_model=ItemResponse)
async def create_item(item: Item):
    result = await collection.insert_one(item.dict())
    new_item = await collection.find_one({"_id": result.inserted_id})
    return item_helper(new_item)

# PUT запрос: Обновление элемента
@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: str, item: Item):
    result = await collection.update_one(
        {"_id": ObjectId(item_id)}, {"$set": item.dict()}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = await collection.find_one({"_id": ObjectId(item_id)})
    return item_helper(updated_item)

# DELETE запрос: Удаление элемента
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)