from typing import List

from sqlalchemy.orm import Session

from models import notesmodel, usersmodel
from schemas.notesheme import NoteSchema, NoteUpdateSchema


def add_note(
        db: Session,
        current_user: usersmodel,
        note_data: NoteSchema
):
    note: notesmodel = notesmodel(
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
    note: notesmodel = db.query(notesmodel).filter(notesmodel.id == new_note.id).first()
    note.text = new_note.text
    db.commit()
    db.refresh(note)
    return note


def delete_note(
        db: Session,
        note_id: int,
):
    note: notesmodel = db.query(notesmodel).filter(notesmodel.id == note_id).first()
    db.delete(note)
    db.commit()


def get_user_notes(
        db: Session,
        current_user: usersmodel,
) -> List[notesmodel]:
    notes = db.query(notesmodel).filter(notesmodel.owner == current_user).all()
    return notes