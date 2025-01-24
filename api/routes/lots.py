from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from validation_schemas.lots import Lot, LotCreate
from api.utils.lots import create_lot, delete_lot, get_lot, get_lots

router = APIRouter()


@router.get('/lots', response_model=List[Lot])
def readLots(auction_id: UUID = None, db: Session = Depends(get_db)):
    return get_lots(db, auction_id)


@router.get('/lot/{lot_id}', response_model=Lot)
def readLot(lot_id: UUID, db: Session = Depends(get_db)):
    lot = get_lot(db, lot_id)
    if lot is None:
        HTTPException(404, f"lot with id {lot_id} does not exist")
    return lot

@router.delete('/lot/{lot_id}', response_model=Lot)
def readLot(lot_id: UUID, db: Session = Depends(get_db)):
    lot = delete_lot(db, lot_id)
    if lot is None:
        HTTPException(404, f"lot with id {lot_id} does not exist")
    return lot


@router.post('/create_lot', response_model=Lot)
def createLot(lot: LotCreate, db: Session = Depends(get_db)):
    return create_lot(db, lot)