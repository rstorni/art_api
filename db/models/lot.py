from uuid import UUID
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy.sql import func

from db.db_setup import Base
from db.models._mixins import Timestamp

class Lot(Timestamp, Base):
    __tablename__ = 'lots'

    lot_id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    auction_id: Mapped[UUID] = mapped_column(ForeignKey('auctions.auction_id'))
    artwork_id: Mapped[UUID] = mapped_column(ForeignKey('artworks.artwork_id', ondelete='CASCADE'), unique=True)
    low_estimate_price: Mapped[int] = mapped_column(default=0)
    high_estimate_price: Mapped[int] = mapped_column(default=0)
    current_bid: Mapped[UUID] = mapped_column(ForeignKey('bids.bid_id'), nullable=True)

    
    artwork = relationship('Artwork', backref=backref("lots", uselist=False), foreign_keys=[artwork_id])
    current_winning_bid = relationship('Bid', backref=backref("lots", uselist=False), foreign_keys=[current_bid])