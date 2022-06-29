import os
from typing import Optional, List
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from fastapi.params import Depends
from fastapi import HTTPException
from starlette import status

from db import get_db
from models import UserModel
from schemas.usersheme import UserSchema, UserCreateSchema
from utils.security import hash_password
from schemas.tokensheme import TokenSchema

ALGORITHM = 'HS256' #os.environ['ALGORITHM']
SECRET_KEY = 'coolkey' #os.environ['SECRET_KEY']
ACCESS_TOKEN_EXPIRE_MINUTES = 30 #int(os.environ['ACCESS_TOKEN_EXPIRE_MINUTES'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def get_user_by_email(db: Session, email: str) -> Optional[UserModel]:
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_all_users(db: Session) -> List[UserModel]:
    return db.query(UserModel).all()


def add_user(db: Session, user_data: UserCreateSchema) -> UserSchema:
    hashed_password = hash_password(user_data.password)
    db_user = UserModel(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserModel:
    credential_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid JWT',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise credential_exceptions
        token_data = TokenSchema(email=email)
    except JWTError:
        raise credential_exceptions
    user = get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credential_exceptions
    return user
