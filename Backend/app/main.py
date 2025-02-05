from fastapi import FastAPI

from .routers import account_router
from .routers import expence_router
from .dependencies import create_db_and_tables

app = FastAPI()

# Code above omitted 👆

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Code below omitted 👇

app.include_router(account_router)
app.include_router(expence_router)