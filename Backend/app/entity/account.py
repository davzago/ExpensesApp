from sqlmodel import SQLModel, Field
from typing import Optional

class Account(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    mail: Optional[str]

class AccountEntity(Account, table=True):
    __tablename__ = 't_account'
    password: str







   
