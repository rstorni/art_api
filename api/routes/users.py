from uuid import UUID
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from validation_schemas.users import UserCreate, User
from api.utils.users import create_user, get_user, get_users

router = APIRouter()

@router.get('/users', response_model=List[User])
def readUsers(db: Session = Depends(get_db)):
    return get_users(db)

@router.post('/create_user', response_model=User)
def createUser(user: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user)
    return user

@router.get('/user/{user_id}', response_model=User)
def readUser(user_id: UUID, db: Session = Depends(get_db)):
    user = get_user(db, user_id=user_id)
    if user is None:
        HTTPException(404, detail=f"user with id {user_id} not found")
    return user