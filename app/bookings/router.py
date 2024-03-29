from app.bookings.schemas import SchemaBooking, SchemaCreateBooking, SchemaUpdateBooking
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


@router.delete("/{booking_id}")
async def delete_booking(booking_id: int) -> bool:
    return await BookingService.delete(booking_id)


@router.put("/{booking_id}")
async def update_booking(booking_id: int, booking: SchemaUpdateBooking) -> bool:
    return await BookingService.update(
        booking_id,
        user_id=booking.user_id,
        room_id=booking.room_id,
        date_from=booking.date_from,
        date_to=booking.date_to,
        total_days=booking.total_days,
    )


@router.post("")
async def create_booking(
    booking: SchemaCreateBooking, user: Users = Depends(get_current_user)
) -> SchemaBooking:
    return await BookingService.create(
        user_id=user.id,
        room_id=booking.room_id,
        date_from=booking.date_from,
        date_to=booking.date_to,
    )
