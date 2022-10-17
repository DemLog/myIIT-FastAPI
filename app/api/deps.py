from typing import Generator

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.user import User
from app.crud import crud_user


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(id_user: int, db: Session = Depends(get_db)) -> User:
    user = crud_user.user.get(db, id=id_user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
