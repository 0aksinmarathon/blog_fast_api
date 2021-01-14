from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.models.common import TimestampMixin
from app.database import Base


class Article(Base, TimestampMixin):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, auto_increment=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(200))
    body = Column(Text)


