from typing import Optional

from pydantic import BaseModel, EmailStr, Field

USERNAME_LENGTH = 100
PASSWORD_LENGTH = 255
STANDARD_LENGTH = 100
DETAILS_LENGTH = 1000

class User(BaseModel):
    username: str = Field(max_length=USERNAME_LENGTH)
    password: str = Field(max_length=PASSWORD_LENGTH)
    first_name: Optional[str] = Field(max_length=STANDARD_LENGTH)
    last_name: Optional[str] = Field(max_length=STANDARD_LENGTH)
    email: EmailStr = Field(max_length=STANDARD_LENGTH)

# class Auction(BaseModel):
#     auction_id: UUID
#     title: str = Field(max_length=STANDARD_LENGTH)
#     details: Optional[str] = Field(max_length=DETAILS_LENGTH)
#     start_datetime: datetime 
#     end_datetime: datetime

# class ArtWork(BaseModel):
#     artwork_id: UUID
#     name: str = Field(max_length=STANDARD_LENGTH)
#     details: Optional[str] = Field(max_length=DETAILS_LENGTH)
#     artist: Optional[str] = Field(max_length=STANDARD_LENGTH)
#     creation_date: datetime = Field(default_factory=datetime.now())
#     medium: Optional[str] = Field(max_length=STANDARD_LENGTH)
#     dimentions: Optional[str]= Field(max_length=STANDARD_LENGTH)

# class AuctionItem(BaseModel):
#     auction_item_id: UUID
#     auction_id: UUID
#     artwork_id: UUID
#     name: str = Field(max_length=STANDARD_LENGTH)
#     details: str = Field(max_length=DETAILS_LENGTH)
#     starting_bid: int = Field(ge=0)

# class Bids(BaseModel):
#     bid_id: UUID
#     user_id: UUID
#     auction_item_id: UUID 
#     bid_timestamp: datetime = Field(default_factory=datetime.now())
#     status: str = Field(max_length=STANDARD_LENGTH)
#     bid_amount: int = Field(ge=0)