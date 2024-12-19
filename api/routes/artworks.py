from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db

router = APIRouter()


@router.get('/artworks')
def read_artworks(db: Session = Depends(get_db)):
    pass

@router.get('/artworks/{artwork_id}')
def read_artwork(db: Session = Depends(get_db)):
    pass

@router.post('/create_artwork')
def create_artwork(db: Session = Depends(get_db)):
    pass
