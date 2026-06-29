from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.repositories.user_repository import (
    get_user_by_email,
    create_user,
)
from app.utils.hash import hash_password


def register_user(db: Session, user):

    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role="user"
    )

    return create_user(db, new_user)