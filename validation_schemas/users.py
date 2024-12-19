from uuid import UUID
from typing import Optional 
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

USERNAME_LENGTH = 100
PASSWORD_LENGTH = 255
STANDARD_LENGTH = 100
DETAILS_LENGTH = 1000

class UserBase(BaseModel):
    username: str = Field(max_length=USERNAME_LENGTH)
    password: str = Field(max_length=PASSWORD_LENGTH)
    first_name: Optional[str] = Field(max_length=STANDARD_LENGTH)
    last_name: Optional[str] = Field(max_length=STANDARD_LENGTH)
    email: EmailStr = Field(max_length=STANDARD_LENGTH)
    is_active: bool = Field()

class UserCreate(UserBase):
    ...

class User(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True