from pydantic import BaseModel, Field


class CreateRoleQueryParams(BaseModel):
    name: str = Field(min_length=4, max_length=20)
