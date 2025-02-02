from sqlalchemy import event
from sqlalchemy.orm import Session

from db.models.lot import Lot as Lot
from db.models.bid import Bid as db_BidClass
from validation_schemas.lots import LotCreate

# def get_highest_bid(db: Session, lot_id: str):
#     lot = db.query(db_LotClass).filter(lot_id==db_LotClass.lot_id).first()

#     if not lot:
#         raise  ValueError(f"No lot with {lot_id} found.")

def update_current_bid(db: Session, lot_id: str):
    highest_bid = db.query(db_BidClass).filter(db_BidClass.lot_id == lot_id).order_by(db_BidClass.amount.desc()).first()
    if highest_bid:
        lot = db.query(Lot).filter(Lot.lot_id == lot_id).first()
        if lot:
            lot.current_winning_bid = highest_bid

def get_lot(db: Session, lot_id: str):
    return db.query(Lot).filter(Lot.lot_id == lot_id).first()

def delete_lot(db: Session, lot_id: str):
    lot = db.query(Lot).filter(Lot.lot_id == lot_id).first()
    db.delete(lot)
    db.commit()
    return lot

def get_lots(db: Session, auction_id: str = None):
    if auction_id:
        return db.query(Lot).filter(Lot.auction_id == auction_id).all()
    else:
        return db.query(Lot).all()

def create_lot(db: Session, lot: LotCreate):
    db_lot = Lot(
        auction_id = lot.auction_id,
        artwork_id = lot.artwork_id,
        low_estimate_price = lot.low_estimate_price,
        high_estimate_price = lot.high_estimate_price
    )

    db.add(db_lot)
    db.commit()
    db.refresh(db_lot)
    return db_lot

@event.listens_for(db_BidClass, "after_insert")
def update_current_bid(mapper, connection, target):
    db = Session(bind=connection)
    curent_lot = db.query(Lot).filter(Lot.lot_id == target.lot_id).first()
    curent_lot.current_bid = target.bid_id
    db.add(curent_lot)
    db.commit()