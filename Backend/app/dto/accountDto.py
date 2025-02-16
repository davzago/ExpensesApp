from sqlmodel import SQLModel

class AccountIn(SQLModel):
    username: str
    mail: str
    password: str

class AccountOut(SQLModel):
    username: str

    def __init__(self, username: str):
        self.username = username

class AccountLogIn(SQLModel):
    username: str
    password: str

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password