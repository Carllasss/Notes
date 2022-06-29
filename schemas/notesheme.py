from pydantic import BaseModel


class NoteBaseSchema(BaseModel):
    text: str


class NoteSchema(NoteBaseSchema):
    owner_id: int

    class Config:
        orm_mode = True


class NoteResponseSchema(NoteSchema):
    id: int


class NoteUpdateSchema(NoteBaseSchema):
    id: int