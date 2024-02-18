from datetime import date

from pydantic import BaseModel


class SchemaBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int


class SchemaCreateBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


class SchemaUpdateBooking(BaseModel):
    user_id: int
    room_id: int
    date_from: date
    date_to: date
    total_days: int
