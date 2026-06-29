from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user_model import User
from app.schemas.user_schema import EmployeeResponse
from app.services.auth_service import get_all_employees
from app.utils.auth import get_current_user

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get(
    "/",
    response_model=List[EmployeeResponse]
)
def get_employees(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_employees(db)