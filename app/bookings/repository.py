from app.base.repository import BaseRepository
from app.bookings.models import Bookings


class BookingRepository(BaseRepository):
    model = Bookings
