from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from validation_schemas.bids import BidCreate, Bid
from api.utils.bid import createBid, getBid, getBids

router = APIRouter()


@router.get('/bids', response_model=List[Bid])
def read_bids(db: Session = Depends(get_db)):
    return getBids(db)

@router.get('/bids/{bid_id}', response_model=Bid)
def read_bid(bid_id: str, db: Session = Depends(get_db)):
    bid = getBid(db, bid_id)
    if bid is None:
        HTTPException(404, f"bid with id {bid_id} does not exist")
    return bid


@router.post('/create_bid', response_model=Bid)
def create_bid(bid: BidCreate, db: Session = Depends(get_db)):
        return createBid(bid, db)