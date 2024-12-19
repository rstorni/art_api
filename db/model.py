from datetime import datetime
from uuid import UUID
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy.sql import func


Base = declarative_base()

# class Status(enum.Enum):
#     PENDING = "pending"
#     RECEIVED = "received"
#     COMPLETED = "completed"

class User(Base):
    __tablename__ = 'users'
    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    username: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[Optional[str]] = mapped_column(String(100))
    last_name: Mapped[Optional[str]] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    registration_date: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_date: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"User Id: {self.id}, Name: {self.first_name} {self.last_name}"

# class ArtObject(Base):
#     __tablename__ = "art_objects"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(30))
#     artist: Mapped[str] = mapped_column(String(30))
#     artist_id: Mapped[int] = mapped_column(ForeignKey("artist.id"))
#     medium: Mapped[str] = mapped_column(String(30))


#     def __repr__(self) -> str:
#         return f"Art Object Id: {self.id}, Title: {self.title}"


    
