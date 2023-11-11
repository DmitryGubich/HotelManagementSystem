from app.base.service import BaseService
from app.hotels.repository import HotelRepository


class HotelService(BaseService):
    repository = HotelRepository

    @classmethod
    async def find_all(cls):
        return await cls.repository.find_all()
