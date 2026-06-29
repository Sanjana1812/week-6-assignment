from fastapi import FastAPI

from app.database.connection import engine
from app.models.user_model import Base
from app.routers.auth_router import router

app = FastAPI(
    title="Week 6 Authentication System"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Authentication System Running"
    }