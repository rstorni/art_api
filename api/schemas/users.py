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