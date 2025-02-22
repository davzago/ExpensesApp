from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from ..dto import AccountLogIn
from ..entity import Account
from ..dependencies.session import session
from ..dependencies.auth import auth_user, create_jwt, get_current_user, Token

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


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

@auth_router.get("/users/me/", response_model=Account)
async def read_users_me(
    current_user: Annotated[Account, Depends(get_current_user)],
):
    return current_user
