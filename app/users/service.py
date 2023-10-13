from typing import Annotated

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
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm


class UserService(BaseService):
    repository = UserRepository

    @classmethod
    async def sign_up(cls, user_data: SchemaUserSignUp) -> SchemaUser:
        existing_user = await cls.find_one_or_none(email=user_data.email)

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
    async def login(
        cls, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ) -> Token:
        user = await cls.find_one_or_none(username=form_data.username)
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise UserUnauthorizedException
        return Token(access_token=create_access_token({"sub": user.username}))
