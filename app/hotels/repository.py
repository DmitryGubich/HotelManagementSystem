from app.base.repository import BaseRepository
from app.hotels.models import Hotels


class HotelRepository(BaseRepository):
    model = Hotels
