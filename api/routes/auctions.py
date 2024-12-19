from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db

router = APIRouter()


@router.get('/auctions')
def read_auctions(db: Session = Depends(get_db)):
    pass

@router.get('/auctions/{auction_id}')
def read_auction(db: Session = Depends(get_db)):
    pass

@router.post('/create_auction')
def create_auction(db: Session = Depends(get_db)):
    pass