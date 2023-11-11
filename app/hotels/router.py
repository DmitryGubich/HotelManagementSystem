from app.hotels.schemas import SchemaHotel
from app.hotels.service import HotelService
from fastapi import APIRouter

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("")
async def get_hotels() -> list[SchemaHotel]:
    return await HotelService.find_all()
