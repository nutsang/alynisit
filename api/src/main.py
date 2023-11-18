from typing import Union

from config import settings
from fastapi import FastAPI, File, UploadFile
from pymongo import MongoClient
import aiofiles

from routes import router as book_router

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongo_client = MongoClient(settings.DATABASE_URL)
    print('Connected to MongoDB...')
    app.database = app.mongo_client[settings.MONGO_INITDB_DATABASE]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/single-file/")
async def upload_single_file(file: UploadFile = File(...)):
    print("filename = ",file.filename)
    destination_file_path = "/images/"+file.filename
    print("destination = ",destination_file_path)
    async with aiofiles.open(destination_file_path,'wb') as out_file:
        while content := await file.read(1024):
            await out_file.write(content)
    return {"Result":"OK"}

app.include_router(book_router, tags=["book"], prefix="/book")