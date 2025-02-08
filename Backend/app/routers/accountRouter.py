from fastapi import APIRouter, Depends
from ..entity.account import AccountEntity, Account
from ..dto.accountDto import AccountIn
from ..dependencies.session import session

account_router = APIRouter(
    prefix="/account",
    tags=["account"],
    responses={404: {"description": "Not found"}},
)

@account_router.post("/create")
def create_account(account: AccountIn, session: session):
    db_account = AccountEntity.model_validate(account)
    session.add(db_account)
    session.commit()
    session.refresh(db_account)
    return Account(id=db_account.id, username=db_account.username, mail=db_account.mail)
