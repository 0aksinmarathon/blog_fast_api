from sqlalchemy import Column, Integer, ForeignKey, Text
from app.models.common import TimestampMixin
from app.database import Base


class Comment(Base, TimestampMixin):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    article_id = Column(Integer, ForeignKey("articles.id"))
    body = Column(Text)
