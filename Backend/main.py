from fastapi import FastAPI, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

# MongoDB settings
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "Bullet_Detection"
COLLECTION_NAME = "Bullet_Detection"

# MongoDB connection
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

class Values(BaseModel):
    _id:Optional[str] = None
    latitude:float
    longitutde:float
    bullet_detected:bool
    heart_rate:int
    temperature:int
    vest_id:int
    timestamp:int


# Create an item
@app.post("/items/", response_model=Values)
async def create_item(item: Values):
    result = await collection.insert_one(item.model_dump())
    created_item = await collection.find_one({"_id": result.inserted_id})
    return created_item

# Read all items
@app.get("/items/", response_model=List[Values])
async def read_items():
    items = await collection.find().to_list(1000)
    return items

# Read a single item by ID
@app.get("/items/{item_id}", response_model=Values)
async def read_item(item_id: str):
    item = await collection.find_one({"_id": item_id})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Update an item by ID
@app.put("/items/{item_id}", response_model=Values)
async def update_item(item_id: str, item: Values):
    existing_item = await collection.find_one({"_id": item_id})
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await collection.update_one({"_id": item_id}, {"$set": item.dict()})
    updated_item = await collection.find_one({"_id": item_id})
    return updated_item

# Delete an item by ID
@app.delete("/items/{item_id}", response_model=Values)
async def delete_item(item_id: str):
    item = await collection.find_one({"_id": item_id})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await collection.delete_one({"_id": item_id})
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)