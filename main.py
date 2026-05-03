from fastapi import FastAPI
from database import engine, Base
from models import Character

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "PostgreSQL Connected"}
