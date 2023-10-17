from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .base import Base

DATABASE_URL = "postgresql://anna:mail1234@db:5432/mydatabase"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()