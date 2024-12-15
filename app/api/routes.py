from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db, model

router = APIRouter()

#Misc
@router.get('/')
def index():
    return 'hello world'

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

