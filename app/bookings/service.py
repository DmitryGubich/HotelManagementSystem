from datetime import date

from app.base.service import BaseService
from app.bookings.repository import BookingRepository


class BookingService(BaseService):
    repository = BookingRepository

    @classmethod
    async def create(cls, user_id: int, room_id: int, date_from: date, date_to: date):
        return await cls.repository.create(
            user_id=user_id, room_id=room_id, date_from=date_from, date_to=date_to
        )

    @classmethod
    async def delete(cls, booking_id: int):
        return await cls.repository.delete(model_id=booking_id)

    @classmethod
    async def update(
        cls,
        booking_id: int,
        user_id: int,
        room_id: int,
        date_from: date,
        date_to: date,
        total_days: int,
    ):
        return await cls.repository.update(
            model_id=booking_id,
            user_id=user_id,
            room_id=room_id,
            date_from=date_from,
            date_to=date_to,
            total_days=total_days,
        )
