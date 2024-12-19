
from sqlalchemy.orm import declarative_base


Base = declarative_base()

# class Status(enum.Enum):
#     PENDING = "pending"
#     RECEIVED = "received"
#     COMPLETED = "completed"

# class ArtObject(Base):
#     __tablename__ = "art_objects"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(30))
#     artist: Mapped[str] = mapped_column(String(30))
#     artist_id: Mapped[int] = mapped_column(ForeignKey("artist.id"))
#     medium: Mapped[str] = mapped_column(String(30))


#     def __repr__(self) -> str:
#         return f"Art Object Id: {self.id}, Title: {self.title}"


    
