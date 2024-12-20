from uuid import UUID
from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from db.db_setup import Base
from db.models._mixins import Timestamp
from db.models._model_constants import STANDARD_LENGTH, DETAILS_LENGTH

class Lot(Timestamp, Base):
    __tablename__ = 'lots'

    lot_id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    auction_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    artwork_id: Mapped[UUID] = mapped_column()


    
