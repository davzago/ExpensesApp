from sqlalchemy import Integer, String
from typing import Optional
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from ..dependencies import Base

class Account(Base):
    __tablename__ = 't_account' 
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(20))
    mail: Mapped[Optional[str]] = mapped_column(String(20))
    password: Mapped[str] = mapped_column(String(20))

   
