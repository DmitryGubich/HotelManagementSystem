from fastapi import FastAPI

from app.bookings.router import router as booking_router
from app.rooms.router import router as room_router
from app.users.router import auth_router as auth_router

app = FastAPI(title="Hotel Management System")

app.include_router(auth_router)
app.include_router(booking_router)
app.include_router(room_router)
