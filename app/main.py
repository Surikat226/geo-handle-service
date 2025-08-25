from fastapi import FastAPI, HTTPException
from app.models.coordinates import Coordinates

app = FastAPI(title="Geo Service")

# Временное хранилище (пока без БД)
coordinates_storage = {}


@app.post("/coordinates")
async def save_coordinates(coords: Coordinates):
    """Сохраняем координаты пользователя"""
    coordinates_storage[coords.user_id] = coords.model_dump()
    return {"status": "ok", "saved": coords.model_dump()}


@app.get("/coordinates/{user_id}")
async def get_coordinates(user_id: str):
    """Получаем последние координаты пользователя"""
    if user_id not in coordinates_storage:
        raise HTTPException(status_code=404, detail="User not found")
    return coordinates_storage[user_id]
