from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from sqlalchemy import text

from .routers import account_router
from .routers import expence_router
from .dependencies.engine import  engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    # Shutdown code (if needed)

app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"status": "ok"}


app.include_router(account_router)
app.include_router(expence_router)
