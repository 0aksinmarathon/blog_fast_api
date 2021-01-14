from pydantic import BaseModel
from typing import Optional


class UserCreateModel(BaseModel):
    name: str
    email: str
    password: str
    is_admin: Optional[bool] = False
    is_staff: Optional[bool] = False


class UserUpdateModel(BaseModel):
    name: Optional[str] = None
    is_admin: Optional[bool] = None
    is_staff: Optional[bool] = None


class UserQueryParams:
    query_params = ['name', 'is_admin', 'is_staff']

    def __init__(self, name: Optional[str] = None, is_admin: Optional[bool] = None, is_staff: Optional[bool] = None):
        self.name = name
        self.is_admin = is_admin
        self.is_staff = is_staff


class UserResponseModel(BaseModel):
    name: str
    email: str
    is_admin: bool
    is_staff: bool

    class Config:
        orm_mode = True


class UserInDB(UserResponseModel):
    hashed_password: str
