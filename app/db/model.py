from datetime import date

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class ArtObject(Base):
    __tablename__ = "art_object"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    artist: Mapped[str] = mapped_column(String(30))
    artist_id: Mapped[int] = mapped_column(ForeignKey("artist.id"))
    medium: Mapped[str] = mapped_column(String(30))


    def __repr__(self) -> str:
        return f"Art Object Id: {self.id}, Title: {self.title}"

class Artist(Base):
    __tablename__ = "artist"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    date_of_birth: Mapped[date] = mapped_column()
    date_of_death: Mapped[date] = mapped_column()
    country: Mapped[str] = mapped_column(String(20))

    def __repr__(self) -> str:
        return f"Artist ID: {self.id}, Artist Name: {self.name}"

    
