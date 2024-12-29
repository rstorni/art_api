from typing import List
from uuid import UUID

from fastapi import APIRouter,  Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from validation_schemas.auctions import Auction, AuctionCreate
from api.utils.auctions import create_auction, get_auction, get_auctions


router = APIRouter()

@router.get('/auctions', response_model=List[Auction])
def readAuctions(db: Session = Depends(get_db)):
    return get_auctions(db)


@router.get('/auction/{auction_id}', response_model=Auction)
def readAuction(auction_id: UUID, db: Session = Depends(get_db)):
    auction = get_auction(db, auction_id=auction_id)
    if auction is None:
        HTTPException(404, detail=f"auction with id {auction_id} not found")
    return auction


@router.post('/create_auction', response_model=Auction)
def createAuction(auction: AuctionCreate, db: Session = Depends(get_db)):
    return create_auction(db, auction)