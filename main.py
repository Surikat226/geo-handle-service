from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from datetime import datetime

app = FastAPI(title="Geo Service")

# Временное хранилище (пока без БД)
coordinates_storage: Dict[str, dict] = {}


class Coordinates(BaseModel):
    user_id: str
    latitude: float
    longitude: float
    timestamp: datetime = datetime.utcnow()


@app.post("/coordinates")
async def save_coordinates(coords: Coordinates):
    """Сохраняем координаты пользователя"""
    coordinates_storage[coords.user_id] = coords.dict()
    return {"status": "ok", "saved": coords.dict()}


@app.get("/coordinates/{user_id}")
async def get_coordinates(user_id: str):
    """Получаем последние координаты пользователя"""
    if user_id not in coordinates_storage:
        raise HTTPException(status_code=404, detail="User not found")
    return coordinates_storage[user_id]


@app.get("/health")
async def health_check():
    return {"status": "running"}
