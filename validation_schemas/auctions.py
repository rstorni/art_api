from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

# from db.models.lot import Lot


class AuctionBase(BaseModel):
    name: str = Field(max_length=100)
    details: str = Field(max_length=500)
    start_date: datetime 
    end_date: datetime


class AuctionCreate(AuctionBase):
    ...


class Auction(AuctionBase): 
    auction_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
