from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from db.models._mixins import Timestamp
from db.db_setup import Base


class Wallet(Timestamp, Base):
    __tablename__ = 'wallets'

    wallet_id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    currency: Mapped[str] = mapped_column(default='USD')
    balance: Mapped[int] = mapped_column(default=0)
    status: Mapped[str] = mapped_column(default='OK')

    user = relationship("User", back_populates="wallets")


