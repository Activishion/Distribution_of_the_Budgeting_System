from datetime import datetime
from re import compile

from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr, validator


VALID_CHARACTERS = compile(r'^[а-яА-Яa-zA-Z\-\_]+$')


class UserBaseModel(BaseModel):
    class Config:
        orm_mode = True

    @validator('id')
    def validate_id(cls, value):
        if value < 1:
            raise ValueError('Error id values.')
        return value

    @validator('name', check_fields=False)
    def validate_name(cls, value):
        if not VALID_CHARACTERS.match(value):
            raise HTTPException(
                status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail = 'Name must contain only letters.'
            )
        return value


class UserCreate(UserBaseModel):
    name: str
    email: EmailStr


class UserRead(UserBaseModel):
    id: int
    name: str
    email: EmailStr
    date: datetime
    is_active_subscription: bool


class UserDelete(UserBaseModel):
    id: int
    email: EmailStr
    is_active_subscription: bool
