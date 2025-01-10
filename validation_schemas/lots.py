
from datetime import datetime
from uuid import UUID


from pydantic import BaseModel, Field


class LotBase(BaseModel):
    auction_id: UUID
    artwork_id: UUID
    low_estimate_price: int = Field(gt=0)
    high_estimate_price: int = Field(gt=0)

class LotCreate(LotBase):
    ...

class Lot(LotBase):
    lot_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True




