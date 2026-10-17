import os
from sqlalchemy import URL
from sqlmodel import create_engine

DATABASE_URL = os.getenv("DATABASE_URL") or URL.create(
    "postgresql+psycopg2",
    username=os.getenv("POSTGRES_USER", "exp_own"),
    password=os.getenv("POSTGRES_PASSWORD", "exp_own"),
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=int(os.getenv("POSTGRES_PORT", "5090")),
    database=os.getenv("POSTGRES_DB", "expencedb"),
)
engine = create_engine(DATABASE_URL, pool_pre_ping=True)


