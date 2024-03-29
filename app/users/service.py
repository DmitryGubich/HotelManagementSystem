from typing import Any

from app.base.service import BaseService
from app.users.auth import create_access_token, get_password_hash, verify_password
from app.users.exceptions import (
    BaseException,
    PasswordsDoNotMatchException,
    UserAlreadyExistsException,
    UserUnauthorizedException,
)
from app.users.repository import UserRepository
from app.users.schemas import SchemaUser, SchemaUserSignUp, Token


class UserService(BaseService):
    repository = UserRepository

    @classmethod
    async def sign_up(cls, user_data: SchemaUserSignUp) -> SchemaUser:
        existing_user = await cls.filter(email=user_data.email)

        if existing_user:
            raise UserAlreadyExistsException
        if user_data.password != user_data.repeat_password:
            raise PasswordsDoNotMatchException

        new_user = await cls.create(
            email=user_data.email,
            username=user_data.username,
            hashed_password=get_password_hash(user_data.password),
        )

        if not new_user:
            raise BaseException

        return new_user

    @classmethod
    async def login(cls, data: Any) -> Token:
        user = await cls.filter(username=data.username)
        if not user or not verify_password(data.password, user.hashed_password):
            raise UserUnauthorizedException
        return Token(access_token=create_access_token({"sub": user.username}))
