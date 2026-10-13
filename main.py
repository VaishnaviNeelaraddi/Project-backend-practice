#  main.py
from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()

# @app.get maps GET /  to this function
@app.get("/")
def root():
    return {"message": "Hello Vaishnavi"}

@app.get("/health")
def root():
    return {"status":"ok"}

router = APIRouter(prefix="/name", tags=["name"])

@router.get("/")
def name():
    return ["Alice", "Bob"]