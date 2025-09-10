from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models.coordinates import Coordinates
from loguru import logger

app = FastAPI(title="Geo Service")

# Разрешённые источники (можно указать "*" для теста)
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:5000",
    "http://127.0.0.1:5000",
    "*"  # ⚠️ пока для MVP, потом лучше ограничить
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # откуда можно стучаться
    allow_credentials=True,
    allow_methods=["*"],     # можно ограничить например ["GET", "POST"]
    allow_headers=["*"],     # заголовки
)

# Временное хранилище (пока без БД)
coordinates_storage = {}


@app.post("/coordinates")
async def save_coordinates(coords: Coordinates):
    """Сохраняем координаты пользователя"""
    coordinates_storage[coords.user_id] = coords.model_dump()
    logger.info(f"Получили данные с координатами: {coords}")
    return {"status": "ok", "saved": coords.model_dump()}


@app.get("/coordinates")
async def get_last_cooridinates():
    """Получаем все последние координаты всех пользователей"""
    return list(coordinates_storage.values())


@app.get("/coordinates/{user_id}")
async def get_user_coordinates(user_id: str):
    """Получаем последние координаты пользователя"""
    if user_id not in coordinates_storage:
        raise HTTPException(status_code=404, detail="User not found")
    return coordinates_storage[user_id]
