from sqlalchemy.orm import Session

from db.models.lot import Lot as db_LotClass
from validation_schemas.lots import LotCreate


def get_lot(db: Session, lot_id: str):
    return db.query(db_LotClass).filter(db_LotClass.lot_id == lot_id).first()

def delete_lot(db: Session, lot_id: str):
    lot = db.query(db_LotClass).filter(db_LotClass.lot_id == lot_id).first()
    db.delete(lot)
    db.commit()
    return lot

def get_lots(db: Session, auction_id: str = None):
    if auction_id:
        return db.query(db_LotClass).filter(db_LotClass.auction_id == auction_id).all()
    else:
        return db.query(db_LotClass).all()

def create_lot(db: Session, lot: LotCreate):
    db_lot = db_LotClass(
        auction_id = lot.auction_id,
        artwork_id = lot.artwork_id,
        low_estimate_price = lot.low_estimate_price,
        high_estimate_price = lot.high_estimate_price
    )

    db.add(db_lot)
    db.commit()
    db.refresh(db_lot)
    return db_lot