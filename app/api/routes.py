from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db, model

#API 
router = APIRouter()

@router.get('/')
def index():
    return 'hello world'

@router.get('/artworks')
def getArtworks(db: Session = Depends(get_db)):
    artworks = db.query(model.ArtObject).all()
    for works in artworks:
        print(works.__repr__())
    
    return artworks

@router.get('/artwork/{artwork_id}')
def getArtwork():
    pass