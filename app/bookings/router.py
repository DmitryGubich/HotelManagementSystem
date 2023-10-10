from app.bookings.schemas import SchemaBooking
from app.bookings.service import BookingService
from fastapi import APIRouter

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("")
async def get_bookings() -> list[SchemaBooking]:
    return await BookingService.find_all()


@router.get("/{booking_id}")
async def get_booking(booking_id: int) -> SchemaBooking:
    return await BookingService.find_by_id(booking_id)
