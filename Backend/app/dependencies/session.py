from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from .engine import engine

def get_session():
    with Session(engine) as session:
        yield session

session = Annotated[Session, Depends(get_session)]

