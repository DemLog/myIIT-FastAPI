from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.api import deps
from app import crud
from app.schemas.user import User

router = APIRouter()


@router.get("/account.getInfo")
def get_info() -> Any:
    """
    Получить информацию об аккаунте
    """
    return {}


@router.get("/account.getInfoProfile", response_model=User)
def get_info_profile(user_id: int, db: Session = Depends(deps.get_db)) -> Any:
    """
    Получить информацию о профиле пользователя
    """
    user = crud.crud_user.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404, detail="Такого пользователя не существует в базе данных"
        )
    return user


@router.put("/account.setInfoProfile")
def set_info_profile() -> Any:
    """
    Изменить информацию о профиле пользователя
    """
    return {}
