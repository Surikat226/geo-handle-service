from pydantic import BaseModel
from datetime import datetime, UTC


class Coordinates(BaseModel):
    """
    Модель запроса с данными пользователя, которые принимаются сервисом
    """

    user_id: int
    latitude: float
    longitude: float
    timestamp: datetime = datetime.now(UTC)
