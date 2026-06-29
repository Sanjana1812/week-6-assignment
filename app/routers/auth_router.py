from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserLogin, TokenResponse
from app.services.auth_service import login_user
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
@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(db, user)