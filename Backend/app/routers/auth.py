from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select, where, SQLModel

from ..dto import AccountIn
from ..dependencies import session
from ..entity import AccountEntity
from ..entity import hash_password



auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

SECRET_KEY = "15676eb6870c3a7cb7bcacca4cb4f9995da7d2f123d6a17aa2ea054151b7ab9c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@auth_router.post("/", )
async def authorize_session(account: AccountIn, session: session):
    if auth_user(account, session):
        return create_jwt() 
    else:
        return status.HTTP_401_UNAUTHORIZED


def create_jwt():
    return ""

def auth_user(account: AccountIn, session: session):
    user = session.select(AccountEntity).where(AccountEntity.username == account.username,
                                                    AccountEntity.password == hash_password(account.password))
    if user:
        return True
    else:
        return False
    

class Token(BaseModel):
    access_token: str
    token_type: str