from sqlmodel import SQLModel

class AccountIn(SQLModel):
    username: str
    mail: str
    password: str