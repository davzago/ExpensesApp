from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import select, SQLModel
from datetime import datetime, timezone, timedelta
from typing import Annotated
import jwt

from ..dto import AccountIn
from ..dependencies.session import session
from ..entity import AccountEntity
from ..entity.account import hash_password



auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

class Token(SQLModel):
    access_token: str
    token_type: str

class AccountLogIn(SQLModel):
    username: str
    password: str

    def __init__(self, username: str, password: str):
        self.username=username
        self.password=password
    

SECRET_KEY = "15676eb6870c3a7cb7bcacca4cb4f9995da7d2f123d6a17aa2ea054151b7ab9c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_jwt(username: str):
    expiretime = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"user":username, "exp":expiretime}
    return Token(access_token=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM), token_type="bearer")


def auth_user(account: AccountLogIn, session: session):
    statement = select(AccountEntity).where(AccountEntity.username == account.username)
    user = session.exec(statement).first()

    if user and user.password == hash_password(account.password):
        return True
    else:
        return False
    
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    decoded_data = jwt.decode(token, SECRET_KEY, [ALGORITHM])
    user_mock = AccountLogIn("banana", "banana")
    if decoded_data:
        decoded_data.username == "banana"
        return user_mock
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    

@auth_router.post("/token")
async def authorize_session(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: session) -> Token:
    AccountLogIn(form_data.username, form_data.password)
    if auth_user(form_data, session):
        return create_jwt(account.username) 
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

@auth_router.get("/users/me/", response_model=AccountIn)
async def read_users_me(
    current_user: Annotated[AccountIn, Depends(get_current_user)],
):
    return current_user
