from app.users.models import Users
from sqladmin import ModelView


class UserAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email, Users.username, Users.bookings]
    column_details_exclude_list = [Users.hashed_password]
    name_plural = "Users"
