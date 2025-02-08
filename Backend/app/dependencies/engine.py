from sqlmodel import create_engine

postgres_url = "postgresql://exp_own:exp_own@localhost:5090/expencedb"

engine = create_engine(postgres_url)



