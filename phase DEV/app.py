# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
async def read_status():
    return {"status": "OK"}
