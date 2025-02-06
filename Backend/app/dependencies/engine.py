from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

postgres_url = "postgresql://exp_own:exp_own@localhost:5090/expencedb"

engine = create_engine(postgres_url)

Base = declarative_base()



