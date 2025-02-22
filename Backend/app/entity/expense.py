from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional, TYPE_CHECKING

from ..dto.expenseDto import ExpenseIn


if TYPE_CHECKING:
    from .account import AccountEntity 

class ExpenseEntity(SQLModel, table=True):
    __tablename__ = "t_expense"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    category: str
    exp_description: Optional[str]
    exp_amount: float
    exp_date: date

    account_id: int = Field(foreign_key="t_account.id")
    account: "AccountEntity" = Relationship(back_populates="expenses")
    
    def __init__(self, expense: ExpenseIn, account_id: int):
        self.category = expense.category
        self.exp_description = expense.exp_description
        self.exp_amount = expense.exp_amount
        self.exp_date = expense.exp_date
        self.account_id = account_id