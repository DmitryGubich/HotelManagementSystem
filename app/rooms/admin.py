from app.rooms.models import Rooms
from sqladmin import ModelView


class RoomsAdmin(ModelView, model=Rooms):
    column_list = [c.name for c in Rooms.__table__.c] + [Rooms.hotel, Rooms.bookings]
    name_plural = "Rooms"
