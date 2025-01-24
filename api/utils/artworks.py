from sqlalchemy.orm import Session

from db.models.artwork import Artwork as db_ArtworkClass
from validation_schemas.artworks import ArtworkCreate


def get_artwork(db: Session, artwork_id: str):
    return db.query(db_ArtworkClass).filter(db_ArtworkClass.artwork_id == artwork_id).first()

def delete_artwork(db: Session, artwork_id: str):
    artwork = db.query(db_ArtworkClass).filter(db_ArtworkClass.artwork_id == artwork_id).first()
    db.delete(artwork)
    db.commit()
    return artwork

def get_artworks(db: Session):
    return db.query(db_ArtworkClass).all()

def create_artwork(db: Session, artwork: ArtworkCreate):
    db_artwork = db_ArtworkClass(
        title = artwork.title, 
        artist = artwork.artist, 
        medium = artwork.medium, 
        details = artwork.details, 
        fabricated_date = artwork.fabricated_date
        )
    
    db.add(db_artwork)
    db.commit()
    db.refresh(db_artwork)
    return db_artwork
    