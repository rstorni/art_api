from uuid import UUID
from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from db.models._model_constants import STANDARD_LENGTH, DETAILS_LENGTH
from db.db_setup import Base
from db.models._mixins import Timestamp

class Auction(Timestamp, Base):
    __tablename__ = 'auctions'

    auction_id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    name: Mapped[str] = mapped_column(String(STANDARD_LENGTH))
    details: Mapped[str] = mapped_column(String(DETAILS_LENGTH))
    start_date: Mapped[datetime] = mapped_column()
    end_date: Mapped[datetime] = mapped_column()

    def __repr__(self) -> str:
        return f"Auction ID: {self.auction_id}, Auction Name: {self.name}"
