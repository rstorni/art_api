from uuid import UUID
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from db.models._model_constants import STANDARD_LENGTH, PASSWORD_LENTH
from db.db_setup import Base
from db.models._mixins import Timestamp

class User(Timestamp, Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    username: Mapped[str] = mapped_column(String(STANDARD_LENGTH))
    password: Mapped[str] = mapped_column(String(PASSWORD_LENTH))
    first_name: Mapped[Optional[str]] = mapped_column(String(STANDARD_LENGTH))
    last_name: Mapped[Optional[str]] = mapped_column(String(STANDARD_LENGTH))
    email: Mapped[str] = mapped_column(String(STANDARD_LENGTH))
    is_active: Mapped[bool] = mapped_column()

    def __repr__(self) -> str:
        return f"User Id: {self.id}, Name: {self.first_name} {self.last_name}"
