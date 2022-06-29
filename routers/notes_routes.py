from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from crud import note_crud
from crud.user_crud import get_current_user
from db import get_db
from models import UserModel
from schemas.notesheme import NoteUpdateSchema, NoteBaseSchema, NoteResponseSchema

note_router = APIRouter()


@note_router.get('', response_model=List[NoteResponseSchema])
def get_my_notes(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    notes = note_crud.get_user_notes(db, current_user)
    return notes


@note_router.post('', response_model=List[NoteResponseSchema])
def add_note(
        note_data: NoteBaseSchema,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user),
):
    note_crud.add_note(
        db,
        current_user,
        note_data,
    )
    notes = note_crud.get_user_notes(db, current_user)
    return notes


@note_router.put('', response_model=List[NoteResponseSchema])
def update_note(
        note_data: NoteUpdateSchema,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user),
):
    note_crud.update_note(
        db,
        new_note=note_data,
    )
    notes = note_crud.get_user_notes(db, current_user)
    return notes


@note_router.delete('/{note_id:int}', response_model=List[NoteResponseSchema])
def delete_note(
        note_id: int,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user),
):
    note_crud.delete_note(db, note_id)
    notes = note_crud.get_user_notes(db, current_user)
    return notes
