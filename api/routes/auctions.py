from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter,  Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from validation_schemas.auctions import Auction, AuctionCreate
from api.utils.auctions import create_auction, delete_auction, get_auction, get_auctions


router = APIRouter()

@router.get('/auctions', response_model=List[Auction])
def readAuctions(num_items: Optional[int] = None, db: Session = Depends(get_db)):
    return get_auctions(db, num_items)

@router.get('/auction/{auction_id}', response_model=Auction)
def readAuction(auction_id: UUID, db: Session = Depends(get_db)):
    auction = get_auction(db, auction_id=auction_id)
    if auction is None:
        HTTPException(404, detail=f"auction with id {auction_id} not found")
    return auction

@router.delete('/auction/{auction_id}', response_model=Auction)
def readAuction(auction_id: UUID, db: Session = Depends(get_db)):
    auction = delete_auction(db, auction_id=auction_id)
    if auction is None:
        HTTPException(404, detail=f"auction with id {auction_id} not found")
    return auction

@router.post('/create_auction', response_model=Auction)
def createAuction(auction: AuctionCreate, db: Session = Depends(get_db)):
    return create_auction(db, auction)