from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from validation_schemas.artworks import ArtworkCreate, Artwork
from api.utils.artworks import create_artwork, get_artwork, get_artworks

router = APIRouter()


@router.get('/artworks', response_model=List[Artwork])
def readArtworks(db: Session = Depends(get_db)):
    return get_artworks(db)

@router.get('/artwork/{artwork_id}', response_model=Artwork)
def readArtwork(artwork_id: UUID, db: Session = Depends(get_db)):
    artwork = get_artwork(db, artwork_id=artwork_id)
    if artwork is None:
        HTTPException(404, detail=f"artwork with id {artwork_id} not found")
    return artwork

@router.post('/create_artwork', response_model=Artwork)
def createArtwork(artwork: ArtworkCreate, db: Session = Depends(get_db)):
    return create_artwork(db, artwork)
    
