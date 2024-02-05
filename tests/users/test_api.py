import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email, password, code",
    [
        ("test@gmail.com", "1234", 201),
        ("test@gmail.com", "12345", 409),
        ("abcde", "12345", 422),
    ],
)
async def test_sign_up(ac: AsyncClient, email, password, code):
    response = await ac.post(
        "auth/sign-up",
        json={
            "email": email,
            "username": "test",
            "password": password,
            "repeat_password": "1234",
        },
    )
    assert response.status_code == code


@pytest.mark.parametrize(
    "username, password, code",
    [
        ("test-example", "test", 200),
        ("admin-example", "test", 200),
    ],
)
async def test_login(ac: AsyncClient, username, password, code):
    response = await ac.post(
        "auth/login",
        json={
            "username": username,
            "password": password,
        },
    )
    assert response.status_code == code
