from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..entity.expense import ExpenseEntity
from ..dto import ExpenseIn
from ..dependencies.session import session

expense_router = APIRouter(
    prefix="/expense",
    tags=["expense"],
    responses={404: {"description": "Not found"}},
)

@expense_router.post("/add", response_model=ExpenseEntity)
def add_expense(expense: ExpenseIn, session: session):
    db_expense = ExpenseEntity.model_validate(expense)
    session.add(db_expense)
    session.commit()
    session.refresh(db_expense)
    return db_expense


@expense_router.get(path="/getall/{account_id}/{limit}/{offset}")
def get_expense(account_id: int, session: session, limit:int = 20, offset: int = 0):
    expenses = session.query(ExpenseEntity).filter(ExpenseEntity.account_id == account_id).order_by(ExpenseEntity.exp_date.desc()).limit(limit).offset(offset).all()
    if not expenses:
        raise HTTPException(404, "No Expense Found")
    return expenses


# @expense_router.post("/update")
# def update_update