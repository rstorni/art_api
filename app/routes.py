from fastapi import APIRouter, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.db import get_db, schema


#DATABASE LOGIC
engine = create_engine('postgresql://localhost:5432/art_db', echo=True)


#API 
router = APIRouter()

@router.get('/')
def index():
    return 'hello world'

@router.get('/art')
def getArt(db: Session = Depends(get_db)):
    artworks = db.query(schema.ArtObject).all()
    for works in artworks:
        print(works.__repr__())
    
    return artworks