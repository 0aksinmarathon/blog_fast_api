from pydantic import BaseModel
from typing import Optional


class ArticleCreateModel(BaseModel):
    id: int
    user_id: int
    title: str
    body: str


class ArticleQueryParams:
    query_params = ['id', 'user_id', 'title', 'body']

    def __init__(self,
                 id: Optional[int] = None,
                 user_id: Optional[int] = None,
                 title: Optional[str] = None,
                 body: Optional[str] = None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.body = body


class ArticleGetResponseModel(BaseModel):
    id: int
    user_id: int
    title: str
    body: str

    class Config:
        orm_mode = True
