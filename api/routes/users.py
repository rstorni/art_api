from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db
from api.schemas.users import User

router = APIRouter()

list_users = []

@router.get('/users', response_model=List[User])
def getUsers(db: Session = Depends(get_db)):
    return list_users

@router.post('/create_user')
def createUser(user: User, db: Session = Depends(get_db)):
    list_users.append(user)
    return user

@router.get('/user/{user_id}', response_model=User)
def getUser(user_id: str, db: Session = Depends(get_db)):
    pass