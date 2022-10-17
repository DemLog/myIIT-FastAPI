from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/account.getInfo")
def get_info() -> Any:
    """
    Получить информацию об аккаунте
    """
    return {}


@router.get("/account.getInfoProfile")
def get_info_profile() -> Any:
    """
    Получить информацию о профиле пользователя
    """
    return {}


@router.put("/account.setInfoProfile")
def set_info_profile() -> Any:
    """
    Изменить информацию о профиле пользователя
    """
    return {}
