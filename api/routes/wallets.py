from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from api.utils.wallets import get_wallets


router = APIRouter()

@router.get('/wallets')
def readWallets(db: Session = Depends(get_db)):
    return get_wallets(db)

# @router.post()