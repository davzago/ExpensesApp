from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

from ..dependencies.hash import hash_context


if TYPE_CHECKING:
    from .expence import ExpenceEntity 

class Account(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    mail: Optional[str]

class AccountEntity(Account, table=True):
    __tablename__ = 't_account'
    password: str

    expences: List["ExpenceEntity"] = Relationship(back_populates="account")



def hash_password(password: str):
    return hash_context.hash(password)
    







   
