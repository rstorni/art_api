from sqlalchemy.orm import Session

from db.models.bid import Bid as db_BidClass
from validation_schemas.bids import BidCreate

def getBid(db: Session, bid_id: str):
    return db.query(db_BidClass).filter(db_BidClass.bid_id == bid_id).first()

def getBids(db: Session):
    return db.query(db_BidClass).all()

def createBid(bid: BidCreate, db: Session):
    db_bid = db_BidClass(
        user_id = bid.user_id,
        # lot_id = bid.lot_id,
        amount = bid.amount,
    )
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)
    return db_bid