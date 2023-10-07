from app.base.service import BaseService
from app.users.repository import UserRepository


class UserService(BaseService):
    repository = UserRepository
