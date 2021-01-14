from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from models.article import Article
from blog_db import get_db_session
from typing import List
from schemas.article import ArticleQueryParams, ArticleGetResponseModel, ArticleCreateModel

router = APIRouter()


@router.get('/{article_id}')
async def get_article(article_id: int, db_session: Session = Depends(get_db_session)):
    return db_session.query(Article).get(article_id)


@router.get('/', response_model=List[ArticleGetResponseModel])
async def get_articles(query_param_values: ArticleQueryParams = Depends(),
                       db_session: Session = Depends(get_db_session)):
    articles = db_session.query(Article)
    for key in query_param_values.query_params:
        if getattr(query_param_values, key) is not None:
            articles = articles.filter(getattr(Article, key) == getattr(query_param_values, key))
    return articles.all()


@router.post('/')
async def create_article(article: ArticleCreateModel, db_session: Session = Depends(get_db_session)):
    new_article = Article(**dict(article))
    db_session.add(new_article)
    db_session.commit()
    return article
