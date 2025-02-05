from fastapi import APIRouter, Depends
from ..model.account import Account, AccountModel
from ..dependencies.session import session

account_router = APIRouter(
    prefix="/account",
    tags=["account"],
    responses={404: {"description": "Not found"}},
)

@account_router.post("/create", response_model=Account)
def create_account(account: AccountModel, session: session):
    db_account = AccountModel.model_validate(account)
    session.add(db_account)
    session.commit()
    session.refresh(db_account)
    return db_account

# @account_router



# @router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}


# @router.get("/users/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}



# @app.post("/heroes/", response_model=HeroPublic)
# def create_hero(hero: HeroCreate, session: SessionDep):
#     db_hero = Hero.model_validate(hero)
#     session.add(db_hero)
#     session.commit()
#     session.refresh(db_hero)
#     return db_hero