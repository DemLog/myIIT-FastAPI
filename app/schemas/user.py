from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    pass


# Properties to receive via API on creation
class UserCreate(UserBase):
    login: str
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    patronymic: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    status: Optional[str] = None
    study_group: Optional[str] = None
    direction: Optional[str] = None
    profile: Optional[str] = None
    form_study: Optional[str] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    is_active: Optional[bool] = True
    is_admin: bool = False


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    login: str
    password: str
