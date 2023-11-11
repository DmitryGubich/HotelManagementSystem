from app.exceptions import BaseException
from fastapi import status


class RoomFullyBooked(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "There is no room left"
