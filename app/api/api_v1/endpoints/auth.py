from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.post("/auth.register")
def register_user() -> Any:
    """
    Регистрация пользователя в системе
    """
    return {}


@router.post("/auth.login")
def login_user() -> Any:
    """
    Авторизация пользователя в системе
    """
    return {}
