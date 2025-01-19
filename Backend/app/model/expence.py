from sqlmodel import SQLModel, Field
import datetime

class Expence(SQLModel, table=True):
    __tablename__ = "t_expence"
    
    id: int = Field(primary_key=True)
    username: str
    category: str
    exp_description: str
    exp_amount: float
    exp_date: datetime