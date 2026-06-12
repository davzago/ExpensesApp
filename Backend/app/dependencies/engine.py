import os
from sqlmodel import create_engine

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://exp_own:exp_own@localhost:5090/expencedb")
engine = create_engine(DATABASE_URL)



