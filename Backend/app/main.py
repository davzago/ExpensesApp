from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from .routers import account_router
from .routers import expense_router
from .dependencies.engine import  engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    # Shutdown code (if needed)

app = FastAPI(lifespan=lifespan)


app.include_router(account_router)
app.include_router(expense_router)