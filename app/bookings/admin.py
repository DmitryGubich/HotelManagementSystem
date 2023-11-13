from app.bookings.models import Bookings
from sqladmin import ModelView


class BookingsAdmin(ModelView, model=Bookings):
    column_list = [c.name for c in Bookings.__table__.c] + [
        Bookings.user,
        Bookings.room,
    ]
    name_plural = "Bookings"
