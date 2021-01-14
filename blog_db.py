from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_SYSTEM = 'mysql'
DB_USER = 'root'
DB_PASSWORD = ''
DB_HOST = 'db'
DB_NAME = 'blog'

SQLALCHEMY_DATABASE_URI = f'{DB_SYSTEM}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():
    try:
        db_session = SessionLocal()
        yield db_session
    finally:
        db_session.close()
