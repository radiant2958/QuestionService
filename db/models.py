from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class Question(Base):
    __tablename__ ='questions'

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String)
    answer_text = Column(String)
    creation_date = Column(DateTime,default=datetime.utcnow)


