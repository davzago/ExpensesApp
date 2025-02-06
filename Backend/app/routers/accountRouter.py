from fastapi import APIRouter, Depends
from ..entity.account import Account
from ..dto.accountDto import AccountIn, AccountOut
from ..dependencies.session import session

account_router = APIRouter(
    prefix="/account",
    tags=["account"],
    responses={404: {"description": "Not found"}},
)

@account_router.post("/create")
def create_account(account: AccountIn, session: session):
    db_account = Account(username=account.username, password=account.password)
    session.add(db_account)
    session.commit()
    session.refresh(db_account)
    return AccountOut(username=db_account.username)

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