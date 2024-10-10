from pydantic import BaseModel, Field


class CreateCommentBodyParams(BaseModel):
    post_id: int
    owner_id: int
    content: str = Field(min_length=10, max_length=300)


class GetCommentsQueryParams(BaseModel):
    post_id: int


class UpdateCommentBodyParams(BaseModel):
    content: str = Field(min_length=10, max_length=300)
