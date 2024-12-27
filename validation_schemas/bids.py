from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field

class BidBase(BaseModel):
    user_id: UUID 
    # lot_id: UUID = Field()
    amount: int = Field(gt=0)

class BidCreate(BidBase):
    ...

class Bid(BidBase):
    bid_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True