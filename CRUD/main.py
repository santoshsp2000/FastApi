from fastapi import FastAPI
import model
from config import engine
import router
import os
from dotenv import load_dotenv

model.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get('/')
async def home():
    return "Hello San"


app.include_router(router.router, prefix='/book', tags=['book'])
