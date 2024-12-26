from uuid import UUID
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class ArtworkBase(BaseModel):
    title: str = Field(max_length=100)
    artist: Optional[str] = Field(max_length=100)
    medium: str = Field(max_length=100)
    details: Optional[str] = Field(max_length=500)
    fabricated_date: Optional[datetime] 


class ArtworkCreate(ArtworkBase):
    ...


class Artwork(ArtworkBase):
    artwork_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
