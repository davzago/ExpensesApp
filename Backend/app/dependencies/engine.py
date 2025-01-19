from sqlmodel import create_engine

postgres_url = "postgresql://exp_own:exp_own@localhost:5090/expencedb"

engine = create_engine(postgres_url, echo=True)

# def create_account():
#     account = Account(username="Banana", user_password="Password")

#     with Session(engine) as session:
#         session.add(account)

#         session.commit()

# create_account()
