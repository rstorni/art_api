from sqlalchemy.orm import Session

from db.models.auction import Auction as db_AuctionClass
from validation_schemas.auctions import AuctionCreate

def get_auctions(db: Session, num_items: int):
    return db.query(db_AuctionClass).limit(num_items).all()


def get_auction(db: Session, auction_id: str):
    return db.query(db_AuctionClass).filter(db_AuctionClass.auction_id == auction_id).first()

def delete_auction(db: Session, auction_id: str):
    auction = db.query(db_AuctionClass).filter(db_AuctionClass.auction_id == auction_id).first()
    db.delete(auction)
    db.commit()
    return auction

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