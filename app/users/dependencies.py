from typing import Annotated

from app.config import settings
from app.users.exceptions import (
    AuthorizationTokenNotFoundException,
    UserNotFoundException,
)
from app.users.models import Users
from app.users.service import UserService
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> Users:
    if not token:
        raise AuthorizationTokenNotFoundException

    payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    username: str = payload.get("sub")

    user = await UserService.filter(username=username)

    if not user:
        raise UserNotFoundException

    return user
