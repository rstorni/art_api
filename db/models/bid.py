from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db_setup import Base
from db.models._mixins import Timestamp



class Bid(Timestamp, Base):
    __tablename__ = 'bids'

    bid_id: Mapped[UUID] = mapped_column(primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    amount: Mapped[int] = mapped_column()


    user = relationship("User", back_populates="bids")





