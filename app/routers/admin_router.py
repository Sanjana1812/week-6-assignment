from fastapi import APIRouter, Depends

from app.models.user_model import User
from app.utils.auth import get_current_admin

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/")
def admin_dashboard(
    current_admin: User = Depends(get_current_admin)
):
    return {
        "message": "Welcome Admin",
        "admin": current_admin.username
    }