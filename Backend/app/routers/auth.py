from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import select, SQLModel
from datetime import datetime, timezone, timedelta
from typing import Annotated
import jwt

from ..dto import AccountIn, AccountOut, AccountLogIn
from ..dependencies.session import session
from ..entity import AccountEntity
from ..entity.account import hash_password, verify_password



auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

class Token(SQLModel):
    access_token: str
    token_type: str
    

SECRET_KEY = "15676eb6870c3a7cb7bcacca4cb4f9995da7d2f123d6a17aa2ea054151b7ab9c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def create_jwt(username: str):
    expiretime = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"user":username, "exp":expiretime}
    return Token(access_token=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM), token_type="bearer")


def auth_user(account: AccountLogIn, session: session):
    statement = select(AccountEntity).where(AccountEntity.username == account.username)
    user = session.exec(statement).first()

    print(user.password)
    print(hash_password(account.password))

    if user and verify_password(account.password, hash_password(account.password)):
        return True
    else:
        return False
    
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: session):
    decoded_data = jwt.decode(token, SECRET_KEY, [ALGORITHM])
    print(decoded_data)
    statement = select(AccountEntity).where(AccountEntity.username == decoded_data.get("user"))
    account = session.exec(statement).first()
    if account: 
        return AccountOut(account.username)
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    

@auth_router.post("/token")
async def authorize_session(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: session) -> Token:
    user_in = AccountLogIn(form_data.username, form_data.password)
    if auth_user(user_in, session):
        return create_jwt(user_in.username) 
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

@auth_router.get("/users/me/", response_model=AccountOut)
async def read_users_me(
    current_user: Annotated[AccountOut, Depends(get_current_user)],
):
    return current_user
