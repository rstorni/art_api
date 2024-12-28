from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from validation_schemas.bids import BidCreate, Bid
from api.utils.bid import get_bid, get_bids, create_bid

router = APIRouter()


@router.get('/bids', response_model=List[Bid])
def readBids(db: Session = Depends(get_db)):
    return get_bids(db)

@router.get('/bids/{bid_id}', response_model=Bid)
def readBid(bid_id: UUID, db: Session = Depends(get_db)):
    bid = get_bid(db, bid_id)
    if bid is None:
        HTTPException(404, f"bid with id {bid_id} does not exist")
    return bid


@router.post('/create_bid', response_model=Bid)
def createBid(bid: BidCreate, db: Session = Depends(get_db)):
        return create_bid(bid, db)