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
    # current_winning_bid: Mapped[UUID] = mapped_column(ForeignKey('bid.bid_id'), nullable=True)

    
    
    artwork = relationship('Artwork', backref=backref("lots", uselist=False))
    # current_winning_bid = relationship("Bid", backref=backref("lots", uselist=False), foreign_keys=[current_winning_bid])



#ale auction  
# 2c863af5-a657-46c1-943f-b8c998f9c868

# Ales sock 
# ae0b856e-4f29-456d-a1eb-cf38a6844f1e