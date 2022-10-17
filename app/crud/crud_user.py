from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserInDB


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_login(self, db: Session, *, login: str) -> Optional[User]:
        return db.query(User).filter(User.login == login).first()

    def create(self, db: Session, *, obj_in: UserInDB) -> User:
        db_obj = User(
            login=obj_in.login,
            password=obj_in.password,
            email=obj_in.email,
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            patronymic=obj_in.patronymic,
            country=obj_in.country,
            city=obj_in.city,
            status=obj_in.status,
            study_group=obj_in.study_group,
            direction=obj_in.direction,
            profile=obj_in.profile,
            form_study=obj_in.form_study,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)
