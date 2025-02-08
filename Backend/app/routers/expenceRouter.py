from fastapi import APIRouter, Depends
from ..entity.expence import ExpenceEntity
from ..dto.expenceDto import ExpenceIn
from ..dependencies.session import session

expence_router = APIRouter(
    prefix="/expence",
    tags=["expence"],
    responses={404: {"description": "Not found"}},
)

@expence_router.post("/add", response_model=ExpenceEntity)
def add_expence(expence: ExpenceIn, session: session):
    db_expence = ExpenceEntity.model_validate(expence)
    session.add(db_expence)
    session.commit()
    session.refresh(db_expence)
    return db_expence