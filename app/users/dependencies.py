from app.config import settings
from app.exceptions import EntityNotFoundException
from app.users.exceptions import AuthorizationTokenNotFoundException
from app.users.service import UserService
from fastapi import Request
from jose import jwt


async def get_current_user(request: Request):
    token = request.headers.get("Authorization")

    if not token:
        raise AuthorizationTokenNotFoundException

    payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    username: str = payload.get("sub")

    user = await UserService.find_one_or_none(username=username)

    if not user:
        raise EntityNotFoundException

    return user
