from sqlalchemy import Boolean, Column, Integer, String
from app.models.common import TimestampMixin
from app.database import Base


class User(Base, TimestampMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, auto_increment=True)
    name = Column(String(128))
    is_admin = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    email = Column(String(128), unique=True, nullable=False)
    hashed_password = Column(String(128))
