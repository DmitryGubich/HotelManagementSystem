from app.base.service import BaseService
from app.rooms.repository import RoomRepository


class RoomService(BaseService):
    repository = RoomRepository

    @classmethod
    async def find_all_rooms(cls, hotel_id: int):
        return await cls.repository.find_all_rooms(hotel_id=hotel_id)
