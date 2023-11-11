from typing import List

from app.rooms.schemas import SchemaRoom
from app.rooms.service import RoomService
from fastapi import APIRouter

router = APIRouter(prefix="", tags=["Rooms"])


@router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id: int) -> List[SchemaRoom]:
    rooms = await RoomService.find_all(hotel_id)
    return rooms
