from fastapi import FastAPI

from app.database.connection import engine
from app.models.user_model import Base

from app.routers.auth_router import router as auth_router
from app.routers.admin_router import router as admin_router


app = FastAPI(
    title="Week 6 Authentication System"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(admin_router)


@app.get("/")
def home():
    return {
        "message": "Authentication System Running"
    }
