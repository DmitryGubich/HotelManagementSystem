from app.base.repository import BaseRepository
from app.rooms.models import Rooms


class RoomRepository(BaseRepository):
    model = Rooms
