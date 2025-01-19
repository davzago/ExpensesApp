from fastapi import FastAPI

from .routers import account_router

app = FastAPI()

app.include_router(account_router)