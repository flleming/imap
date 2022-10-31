from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from api import router
from model import databaseInt, InitUser
from scheduler import app as rocketry_app
import asyncio

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def event_startup():
    logging.info("sql connection....")
    databaseInt()
    await InitUser()
    # schedule = asyncio.create_task(rocketry_app.serve())
    # schedule


@app.on_event("shutdown")
async def event_shutdown():
    logging.info("connection to mongodb has been closed!")


@app.get("/info")
async def root():
    return {"message": "Hello World"}

app.include_router(router)
