from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class Expence(SQLModel):
    username: str
    category: str
    exp_description: str
    exp_amount: float
    exp_date: date


class ExpenceModel(Expence, table=True):
    __tablename__ = "t_expence"
    
    id: Optional[int] = Field(default=None, primary_key=True)