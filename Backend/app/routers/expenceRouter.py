from fastapi import APIRouter, Depends
from ..entity.expence import Expence, ExpenceModel
from ..dependencies.session import session

expence_router = APIRouter(
    prefix="/expence",
    tags=["expence"],
    responses={404: {"description": "Not found"}},
)

@expence_router.post("/add", response_model=Expence)
def add_expence(expence: Expence, session: session):
    db_expence = ExpenceModel.model_validate(expence)
    session.add(db_expence)
    session.commit()
    session.refresh(db_expence)
    return db_expence