import asyncio
import json
from datetime import datetime
from typing import Generator

import pytest
from app.bookings.models import Bookings
from app.database import Base, async_session_maker, engine
from app.hotels.models import Hotels
from app.main import app
from app.rooms.models import Rooms
from app.users.models import Users
from config import settings
from httpx import AsyncClient
from sqlalchemy import insert


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def load_fixture(model: str):
        with open(f"tests/fixtures/{model}_fixture.json", encoding="utf-8") as file:
            return json.load(file)

    hotels = load_fixture("hotels")
    rooms = load_fixture("rooms")
    users = load_fixture("users")
    bookings = load_fixture("bookings")

    for booking in bookings:
        booking["date_from"] = datetime.strptime(booking["date_from"], "%Y-%m-%d")
        booking["date_to"] = datetime.strptime(booking["date_to"], "%Y-%m-%d")

    async with async_session_maker() as session:
        for Model, values in [
            (Hotels, hotels),
            (Rooms, rooms),
            (Users, users),
            (Bookings, bookings),
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
