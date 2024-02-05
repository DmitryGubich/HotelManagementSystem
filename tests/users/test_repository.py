import pytest
from app.users.repository import UserRepository

from users.auth import get_password_hash


@pytest.mark.parametrize(
    "user_id, email, exist",
    [
        (1, "test@test.com", True),
        (2, "admin@example.com", True),
        (4, "sdsffs", False),
    ],
)
async def test_find_user_by_id(user_id, email, exist):
    user = await UserRepository.find_by_id(user_id)
    if exist:
        assert user
        assert user.email == email
    else:
        assert not user


async def test_add_user():
    assert len(await UserRepository.find_all()) == 4
    await UserRepository.create(
        email="email",
        username="username",
        hashed_password=get_password_hash("password"),
    )
    assert len(await UserRepository.find_all()) == 5
