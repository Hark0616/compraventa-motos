# app/main.py
from fastapi import FastAPI
from app.routes import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router)
@app.get("/")
def root():
    return {"message": "API de Compraventa de Motos funcionando 🚀"}
