from pydantic import BaseModel
from typing import Optional


class CommentCreateModel(BaseModel):
    id: int
    user_id: int
    article_id: int
    body: str


class CommentUpdateModel(BaseModel):
    user_id: Optional[int] = None
    article_id: Optional[int] = None
    body: Optional[str] = None


class CommentQueryParams:
    query_params = ['id', 'user_id', 'article_id', 'body']

    def __init__(self,
                 id: Optional[int] = None,
                 user_id: Optional[int] = None,
                 article_id: Optional[int] = None,
                 body: Optional[str] = None):
        self.id = id
        self.user_id = user_id
        self.article_id = article_id
        self.body = body


class CommentGetResponseModel(BaseModel):
    id: int
    user_id: int
    article_id: int
    body: str

    class Config:
        orm_mode = True
