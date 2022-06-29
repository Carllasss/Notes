from typing import List

from sqlalchemy.orm import Session

from models import UserModel, NoteModel
from schemas.notesheme import NoteSchema, NoteUpdateSchema


def add_note(
        db: Session,
        current_user: UserModel,
        note_data: NoteSchema
):
    note: NoteModel = NoteModel(
        text=note_data.text,
    )
    note.owner = current_user
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def update_note(
        db: Session,
        new_note: NoteUpdateSchema,
):
    note: NoteModel = db.query(NoteModel).filter(NoteModel.id == new_note.id).first()
    note.text = new_note.text
    db.commit()
    db.refresh(note)
    return note


def delete_note(
        db: Session,
        note_id: int,
):
    note: NoteModel = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    db.delete(note)
    db.commit()


def get_user_notes(
        db: Session,
        current_user: UserModel,
) -> List[NoteModel]:
    notes = db.query(NoteModel).filter(NoteModel.owner == current_user).all()
    return notes
