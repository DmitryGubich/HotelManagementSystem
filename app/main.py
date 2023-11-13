from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from app.bookings.admin import BookingsAdmin
from app.bookings.router import router as booking_router
from app.database import engine
from app.hotels.admin import HotelsAdmin
from app.hotels.router import router as hotel_router
from app.images.router import router as image_router
from app.rooms.admin import RoomsAdmin
from app.rooms.router import router as room_router
from app.templates.router import router as template_router
from app.users.admin import UserAdmin
from app.users.router import auth_router as auth_router

# app
app = FastAPI(title="Hotel Management System")

# admin
admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(BookingsAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)

# routes
app.include_router(auth_router)
app.include_router(booking_router)
app.include_router(room_router)
app.include_router(hotel_router)
app.include_router(template_router)
app.include_router(image_router)

# static
app.mount("/static", StaticFiles(directory="static"), "static")
