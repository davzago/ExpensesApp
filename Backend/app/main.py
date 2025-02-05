from fastapi import FastAPI
from contextlib import asynccontextmanager

from .routers import account_router
from .routers import expence_router
from .dependencies import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    create_db_and_tables()
    yield
    # Shutdown code (if needed)

app = FastAPI(lifespan=lifespan)

# Code below omitted 👇

app.include_router(account_router)
app.include_router(expence_router)