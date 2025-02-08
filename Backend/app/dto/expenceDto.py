from datetime import date
from typing import Optional
from sqlmodel import SQLModel

class ExpenceIn(SQLModel):
    category: str
    exp_description: Optional[str]
    exp_amount: float
    exp_date: date
    account_id: int