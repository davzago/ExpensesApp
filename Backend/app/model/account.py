from sqlmodel import SQLModel, Field

class Account(SQLModel):
    username: str = Field(primary_key=True)
    person_name: str
    surname: str
    

class AccountModel(Account, table=True):
    __tablename__ = 't_account' 

    user_password: str
