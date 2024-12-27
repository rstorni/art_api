from sqlalchemy.orm import Session

from db.models.auction import Auction as db_AuctionClass
from validation_schemas.auctions import AuctionCreate

def get_auctions(db: Session):
    return db.query(db_AuctionClass).all()

def get_auction(db: Session, auction_id: str):
    return db.query(db_AuctionClass).filter(db_AuctionClass.auction_id == auction_id).first()

def create_auction(db: Session, auction: AuctionCreate):

    db_auction = db_AuctionClass(
        name = auction.name,
        details = auction.details,
        start_date = auction.start_date,
        end_date = auction.end_date
    )

    db.add(db_auction)
    db.commit()
    db.refresh(db_auction)
    return db_auction