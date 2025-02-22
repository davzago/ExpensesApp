from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated
from sqlmodel import select

from ..dependencies.auth import get_current_user
from ..entity.expense import ExpenseEntity
from ..entity.account import Account
from ..dto import ExpenseIn
from ..dependencies.session import session

expense_router = APIRouter(
    prefix="/expense",
    tags=["expense"],
    responses={404: {"description": "Not found"}},
)

@expense_router.post("/add", response_model=ExpenseEntity)
def add_expense(expense: ExpenseIn, current_user: Annotated[Account, Depends(get_current_user)], session: session):
    db_expense = ExpenseEntity(expense, current_user.id)
    session.add(db_expense)
    session.commit()
    session.refresh(db_expense)
    return db_expense

    
@expense_router.get(path="/getall/{limit}/{offset}")
def get_expense(current_user: Annotated[Account, Depends(get_current_user)], session: session, limit: int = 20, offset: int = 0) -> List[ExpenseEntity]:
    statement = select(ExpenseEntity).where(ExpenseEntity.account_id == current_user.id).limit(limit).offset(offset)
    expenses = session.exec(statement).all()
    if not expenses:
        raise HTTPException(404, "No Expense Found")
    return expenses


@expense_router.post("/update/{expense_id}")
def update_update(expense_id: int, updated_expense: ExpenseIn, current_user : Annotated[Account, Depends(get_current_user)], session: session):
    statement = select(ExpenseEntity).where(ExpenseEntity.id == expense_id, ExpenseEntity.account_id == current_user.id)
    db_expense = session.exec(statement).first()
    if not db_expense:
        raise HTTPException(404, "Expense to update not found")
    updated_expense = update_expense(db_expense, updated_expense)
    session.add(updated_expense)
    session.commit()
    session.refresh(updated_expense)
    return updated_expense




def update_expense(old_expense: ExpenseEntity, new_expense: ExpenseIn):
    old_expense.category = new_expense.category
    old_expense.exp_amount = new_expense.exp_amount
    old_expense.exp_date = new_expense.exp_date
    old_expense.exp_description = new_expense.exp_description
    return old_expense

