from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.bookings.router import router as booking_router
from app.hotels.router import router as hotel_router
from app.images.router import router as image_router
from app.rooms.router import router as room_router
from app.templates.router import router as template_router
from app.users.router import auth_router as auth_router

app = FastAPI(title="Hotel Management System")

app.mount("/static", StaticFiles(directory="static"), "static")

app.include_router(auth_router)
app.include_router(booking_router)
app.include_router(room_router)
app.include_router(hotel_router)
app.include_router(template_router)
app.include_router(image_router)
