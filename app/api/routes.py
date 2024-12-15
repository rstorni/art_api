from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db, model

router = APIRouter()

#Misc
@router.get('/')
def index():
    return 'hello world'

#Artists
@router.get('/artists')
def getArtists():
    pass

@router.get('/artist/{artist_id}')
def getArtist():
    pass

@router.patch('/artist/{artist_id}')
def updateArtist():
    pass

@router.post('/artist')
def createArtist():
    pass

#Art Ojects
@router.get('/artworks')
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

