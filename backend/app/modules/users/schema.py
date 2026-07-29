from pydantic import BaseModel, EmailStr
import uuid
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Optional[str] = "free"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    role: str
    created_at: datetime
    updated_at: datetime

    class Config():
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str