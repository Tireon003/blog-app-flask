from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime


class UserID(BaseModel):
    id: int


class ResponseUserSchema(BaseModel):
    id: int
    username: str
    hashed_password: str
    email: EmailStr
    role_id: int
    date_of_birth: datetime | None

    class Config:
        from_attributes = True


class UserCreateBodySchema(BaseModel):
    username: str = Field(min_length=8)
    password: str = Field(min_length=8)
    email: EmailStr
    role_id: int = Field(default=1)
    date_of_birth: datetime | None = Field(default=None)


class UserUpdateBodySchema(BaseModel):
    username: str | None = Field(min_length=8, default=None)
    password: str | None = Field(min_length=8, default=None)
    email: EmailStr | None = Field(default=None)
    role_id: int | None = Field(default=None)
    date_of_birth: datetime | None = Field(default=None)


class UserResponseSchema(BaseModel):
    message: str
    status: int = 200
