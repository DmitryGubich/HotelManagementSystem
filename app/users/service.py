from app.base.service import BaseService
from app.users.auth import create_access_token, get_password_hash, verify_password
from app.users.exceptions import (
    BaseException,
    PasswordsDoNotMatchException,
    UserAlreadyExistsException,
    UserUnauthorizedException,
)
from app.users.repository import UserRepository
from app.users.schemas import SchemaUseLogIn, SchemaUser, SchemaUserSignUp


class UserService(BaseService):
    repository = UserRepository

    @classmethod
    async def sign_up(cls, user_data: SchemaUserSignUp) -> SchemaUser:
        existing_user = await cls.find_one_or_none(email=user_data.email)

        if existing_user:
            raise UserAlreadyExistsException
        if user_data.password != user_data.repeat_password:
            raise PasswordsDoNotMatchException

        hashed_password = get_password_hash(user_data.password)
        new_user = await cls.create(
            email=user_data.email,
            username=user_data.username,
            hashed_password=hashed_password,
        )

        if not new_user:
            raise BaseException

        return new_user

    @classmethod
    async def login(cls, user_data: SchemaUseLogIn) -> str:
        user = await cls.find_one_or_none(email=user_data.email)
        if not user or not verify_password(user_data.password, user.hashed_password):
            raise UserUnauthorizedException
        return create_access_token({"sub": user.id})
