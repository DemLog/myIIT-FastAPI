from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.schemas import user
from app.crud import crud_user
from app.utils.moodle import MoodleAuth

router = APIRouter()


@router.post("/auth.register", response_model=user.User)
async def register_user(*, db: Session = Depends(deps.get_db), user_in: user.UserCreate) -> Any:
    """
    Регистрация пользователя в системе
    """
    _user = crud_user.user.get_by_login(db, login=user_in.login)
    if _user:
        raise HTTPException(
            status_code=400,
            detail="Данный пользователь уже зарегистрирован в системе",
        )
    moodle = MoodleAuth(user_in.login, user_in.password)
    moodle_data = moodle.check_account()
    if 'error_message' in moodle_data:
        raise HTTPException(
            status_code=401,
            detail=moodle_data["error_message"],
        )
    moodle_data |= user_in.dict()
    data_db = user.UserInDB(**moodle_data)
    _user = crud_user.user.create(db, obj_in=data_db)

    return _user


@router.post("/auth.login")
def login_user() -> Any:
    """
    Авторизация пользователя в системе
    """
    return {}
