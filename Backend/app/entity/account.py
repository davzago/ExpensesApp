from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

from ..dependencies.hash import hash_context


if TYPE_CHECKING:
    from .expense import ExpenseEntity 

class Account(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    mail: Optional[str]

class AccountEntity(Account, table=True):
    __tablename__ = 't_account'
    password: str

    expenses: List["ExpenseEntity"] = Relationship(back_populates="account")


def hash_password(password: str):
    return hash_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return hash_context.verify(password, hashed_password)
    







   
