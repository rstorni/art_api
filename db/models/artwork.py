from uuid import UUID
from datetime import datetime
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from db.models._model_constants import STANDARD_LENGTH, DETAILS_LENGTH
from db.db_setup import Base
from db.models._mixins import Timestamp

class Artwork(Timestamp, Base):
    __tablename__ = 'artworks'

    artwork_id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    title: Mapped[str] = mapped_column(String(STANDARD_LENGTH))
    artist: Mapped[Optional[str]] = mapped_column(String(STANDARD_LENGTH))
    medium: Mapped[str] = mapped_column(String(STANDARD_LENGTH))
    details:Mapped[Optional[str]] = mapped_column(String(DETAILS_LENGTH))
    fabricated_date: Mapped[Optional[datetime]] = mapped_column()

    # Relationships
    # lot: Mapped["Lot"] = relationship("Lot", back_populates='artwork')


    def __repr__(self) -> str:
        return f"Artwork Id: {self.artwork_id}, Title: {self.title}, Artist: {self.artist}"