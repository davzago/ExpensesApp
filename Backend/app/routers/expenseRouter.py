from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import select, where
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
def get_expense(account_id: int, session: session, limit: int = 20, offset: int = 0):
    expenses = session.query(ExpenseEntity).filter(ExpenseEntity.account_id == account_id).order_by(ExpenseEntity.exp_date.desc()).limit(limit).offset(offset).all()
    if not expenses:
        raise HTTPException(404, "No Expense Found")
    return expenses


@expense_router.post("/update/{expense_id}")
def update_update(expense_id: int, updated_expense: ExpenseIn):
    db_expense = session.select(ExpenseEntity).where(ExpenseEntity.id == expense_id)
    if not db_expense:
        raise HTTPException(404, "No Expense Found")
    updated_expense = update_expense(db_expense, update_expense())
    session.add(updated_expense)
    session.commit()
    session.refresh(updated_expense)
    return updated_expense




def update_expense(old_expese: ExpenseEntity, new_expense: ExpenseIn):
    old_expese.category = new_expense.category
    old_expese.exp_amount = new_expense.exp_amount
    old_expese.exp_date = new_expense.exp_date
    old_expese.exp_description = new_expense.exp_description
    return old_expese

