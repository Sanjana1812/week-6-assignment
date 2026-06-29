from fastapi import FastAPI

from app.database.connection import engine
from app.models.user_model import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Authentication System Running"
    }