
from fastapi import FastAPI, Depends
import auth
from routes import router as currency_router
from pymongo import MongoClient
from dotenv import dotenv_values
from functools import lru_cache


config = dotenv_values(".env")

app = FastAPI()


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
async def root():
    return {"message": "Welcome to The Currency Converter App"}

app.include_router(currency_router, dependencies=[Depends(auth.get_api_key)])
