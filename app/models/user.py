from sqlalchemy import Boolean, Column, Integer, String

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    patronymic = Column(String, index=True)
    country = Column(String, index=True)
    city = Column(String, index=True)
    status = Column(String, index=True)
    study_group = Column(String, index=True)
    direction = Column(String, index=True)
    profile = Column(String, index=True)
    form_study = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    is_admin = Column(Boolean(), default=False)
