from app.bookings.schemas import SchemaBooking
from app.bookings.service import BookingService
from app.users.dependencies import get_current_user
from app.users.models import Users
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SchemaBooking]:
    return await BookingService.find_all(user_id=user.id)


@router.get("/{booking_id}")
async def get_booking(booking_id: int) -> SchemaBooking:
    return await BookingService.find_by_id(booking_id)
