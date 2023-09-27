from fastapi import FastAPI

from app.bookings.router import router as booking_router

app = FastAPI(title="Hotel Management System")

app.include_router(booking_router)
