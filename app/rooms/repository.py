from app.base.repository import BaseRepository
from app.bookings.models import Bookings
from app.database import async_session_maker
from app.rooms.models import Rooms
from sqlalchemy import func, select


class RoomRepository(BaseRepository):
    model = Rooms

    @classmethod
    async def find_all_rooms(cls, hotel_id: int):
        booked_rooms = (
            select(Bookings.room_id, func.count(Bookings.room_id).label("rooms_booked"))
            .select_from(Bookings)
            .group_by(Bookings.room_id)
            .cte("booked_rooms")
        )

        get_rooms = (
            select(
                Rooms.__table__.columns,
                (Rooms.quantity - func.coalesce(booked_rooms.c.rooms_booked, 0)).label(
                    "rooms_left"
                ),
            )
            .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
            .where(Rooms.hotel_id == hotel_id)
        )

        async with async_session_maker() as session:
            rooms = await session.execute(get_rooms)
            return rooms.mappings().all()
