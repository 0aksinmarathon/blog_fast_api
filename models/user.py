from sqlalchemy import Boolean, Column, Integer, String
from models.common import TimestampMixin
from blog_db import Base


class User(Base, TimestampMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, auto_increment=True)
    name = Column(String(200))
    is_admin = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    email = Column(String(200))
