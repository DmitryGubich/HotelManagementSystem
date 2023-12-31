from app.exceptions import BaseException, EntityNotFoundException
from fastapi import status


class UserAlreadyExistsException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User with given email already exists"


class UserUnauthorizedException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"


class PasswordsDoNotMatchException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Passwords must match"


class AuthorizationTokenNotFoundException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Authorization token was not provided"


class UserNotFoundException(EntityNotFoundException):
    detail = "User does not exist"
