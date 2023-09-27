from app.base.service import BaseService
from app.bookings.repository import BookingRepository


class BookingService(BaseService):
    repository = BookingRepository
