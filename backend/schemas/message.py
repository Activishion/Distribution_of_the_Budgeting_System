from datetime import datetime
from re import compile

from pydantic import BaseModel, validator, Field

from schemas.user import UserRead


LETTER_MATCH_PATTERN = compile(r'^[а-яА-Яa-zA-Z\-\_]+$')


class MessageBaseModel(BaseModel):
    PAO: bool
    DZO: bool
    subject: str = Field(min_length=2)
    message: str = Field(min_length=2)

    class Config:
        orm_mode = True
        anystr_strip_whitespace = True

    @validator('PAO')
    def validate_PAO(cls, value):
        if value not in [True, False, 1, 0]:
            raise ValueError('Value not valid.')
        return value
    
    @validator('DZO')
    def validate_DZO(cls, value):
        if value not in [True, False, 1, 0]:
            raise ValueError('Value not valid.')
        return value


class MessageRead(MessageBaseModel):
    id: int
    date: datetime
    author: UserRead

    @validator('id')
    def validate_id(cls, value):
        if value < 1:
            raise ValueError('Error id values.')
        return value


class MessageCreate(MessageBaseModel):
    pass
