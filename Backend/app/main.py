from fastapi import FastAPI
from contextlib import asynccontextmanager

from .routers import account_router
from .routers import expence_router
from .dependencies.engine import Base, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    Base.metadata.create_all(engine)
    yield
    # Shutdown code (if needed)

app = FastAPI(lifespan=lifespan)


app.include_router(account_router)
app.include_router(expence_router)