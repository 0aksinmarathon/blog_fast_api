from sqlalchemy import Column, Integer, String, ForeignKey, Text
from models.common import TimestampMixin
from blog_db import Base


class Comment(Base, TimestampMixin):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    article_id = Column(Integer, ForeignKey("articles.id"))
    body = Column(Text)
