from sqlalchemy import Column, Integer, String, ForeignKey, Text
from models.common import TimestampMixin
from blog_db import Base


class Article(Base, TimestampMixin):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, auto_increment=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(200))
    body = Column(Text)


