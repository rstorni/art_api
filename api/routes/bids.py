from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db

router = APIRouter()


@router.get('/bids')
def read_bids(db: Session = Depends(get_db)):
    pass

@router.get('/bids/{bid_id}')
def read_bid(db: Session = Depends(get_db)):
    pass

@router.post('/create_bid')
def create_bid(db: Session = Depends(get_db)):
    pass