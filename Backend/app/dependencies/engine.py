from sqlmodel import create_engine, SQLModel

postgres_url = "postgresql://exp_own:exp_own@localhost:5090/expencedb"

engine = create_engine(postgres_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

