from pydantic import BaseModel, Field


class CreatePostBodyParams(BaseModel):
    title: str = Field(min_length=10, max_length=100)
    content: str = Field(min_length=100, max_length=2000)
    author_id: int


class UpdatePostBodyParams(CreatePostBodyParams):
    ...
