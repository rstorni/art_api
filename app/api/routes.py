from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db, model
# from app.api.schemas import User

router = APIRouter()

#Misc
@router.get('/')
def index():
    return 'hello world'

# User
@router.get('/users')
def getUsers(db: Session = Depends(get_db)):
    pass

@router.get('/user/{user_id}')
def getUser(user_id: str, db: Session = Depends(get_db)):
    dbItem = db.query(model.User).where(id==user_id)
    print(dbItem.__repr__())
    return dbItem

@router.post('/create_user')
def createUser(db: Session = Depends(get_db)):
    pass

#Art Ojects
@router.get('/art_objects')
def getArtworks(db: Session = Depends(get_db)):
    artworks = db.query(model.ArtObject).all()
    for works in artworks:
        print(works.__repr__())
    
    return artworks

@router.get('/artwork/{artwork_id}')
def getArtwork():
    pass

@router.post('/artwork')
def createArtwork():
    pass

