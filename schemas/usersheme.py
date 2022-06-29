from typing import List

from pydantic import BaseModel
from pydantic import EmailStr

from schemas.notesheme import NoteSchema


class UserBase(BaseModel):
    email: EmailStr


class UserSchema(UserBase):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserCreateSchema(UserSchema):
    password: str

    class Config:
        orm_mode = False


class UserNotesSchema(UserSchema):
    notes: List[NoteSchema]