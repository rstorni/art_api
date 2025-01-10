from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy.sql import func

from db.db_setup import Base
from db.models._mixins import Timestamp

class Lot(Timestamp, Base):
    __tablename__ = 'lots'

    lot_id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    auction_id: Mapped[UUID] = mapped_column(ForeignKey('auctions.auction_id'))
    artwork_id: Mapped[UUID] = mapped_column(ForeignKey('artworks.artwork_id'), unique=True)
    low_estimate_price: Mapped[int] = mapped_column()
    high_estimate_price: Mapped[int] = mapped_column()
    
    artwork = relationship('Artwork', backref=backref("lots", uselist=False))
    # auction: Mapped["Auction"] = relationship("Auction", back_populates="lot")
    # artwork = relationship("Artwork", back_populates="lot")



#ale auction  
# 2c863af5-a657-46c1-943f-b8c998f9c868

# Ales sock 
# ae0b856e-4f29-456d-a1eb-cf38a6844f1e