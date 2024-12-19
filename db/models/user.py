from uuid import UUID
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from ..db_setup import Base
from .mixins import Timestamp

class User(Timestamp, Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    username: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[Optional[str]] = mapped_column(String(100))
    last_name: Mapped[Optional[str]] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column()

    def __repr__(self) -> str:
        return f"User Id: {self.id}, Name: {self.first_name} {self.last_name}"
