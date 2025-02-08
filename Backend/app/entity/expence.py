from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from .account import AccountEntity 

class ExpenceEntity(SQLModel, table=True):
    __tablename__ = "t_expence"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    category: str
    exp_description: Optional[str]
    exp_amount: float
    exp_date: date

    account_id: int = Field(foreign_key="t_account.id")
    account: "AccountEntity" = Relationship(back_populates="expences")