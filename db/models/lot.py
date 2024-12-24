from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from db.db_setup import Base
from db.models._mixins import Timestamp

class Lot(Timestamp, Base):
    __tablename__ = 'lots'

    lot_id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    auction_id: Mapped[UUID] = mapped_column(ForeignKey('auctions.auction_id'))
    # artwork_id: Mapped[UUID] = mapped_column(ForeignKey('artworks.artwork_id'))
    
    auction = relationship("Auction", back_populates="lot")
    artwork = relationship("Artwork", back_populates="lots")



    
