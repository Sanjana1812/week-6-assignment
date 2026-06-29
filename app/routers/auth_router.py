from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.user_schema import (
    UserRegister,
    UserResponse,
)
from app.services.auth_service import register_user

router = APIRouter(
    prefix="",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(db, user)