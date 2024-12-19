from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db

router = APIRouter()


@router.get('/lots')
def read_lots(db: Session = Depends(get_db)):
    pass

@router.get('/lots/{lot_id}')
def read_lot(db: Session = Depends(get_db)):
    pass

@router.post('/create_lot')
def create_lot(db: Session = Depends(get_db)):
    pass