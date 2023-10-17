from fastapi import APIRouter, Depends, HTTPException
from app.db.session import get_db
from app.db.models import Question
from sqlalchemy.orm import Session
from sqlalchemy import exists
import httpx
from datetime import datetime
router = APIRouter()

async def fetch_question(count: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jservice.io/api/random?count={count}")
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail='Failed to fetch from jservice')
        return response.json()
    
@router.post("/questions/")
async def get_question(questions_num: int, db: Session = Depends(get_db)):
    questions = await fetch_question(questions_num)

    for question in questions:
        is_existing = db.query(exists().where(Question.id == question['id'])).scalar()
        while is_existing:
            questions = await fetch_question(1)
            question = questions[0]
            is_existing = db.query(exists().where(Question.id == question['id'])).scalar()
        
        created_as_str = question.get("created_at")
        created_as_str = created_as_str.rstrip("Z")
        created_at = datetime.fromisoformat(created_as_str)

        db.add(Question(
            id=question['id'],
            question_text=question['question'], 
            answer_text=question['answer'],
            creation_date=created_at))
        db.commit()

    # Получаем последние добавленные вопросы из базы данных
    last_questions = db.query(Question).order_by(Question.creation_date.desc()).limit(questions_num).all()

    return [{
        "id": q.id,
        "question_text": q.question_text,
        "answer_text": q.answer_text,
        "creation_date": q.creation_date   
    } for q in last_questions]
