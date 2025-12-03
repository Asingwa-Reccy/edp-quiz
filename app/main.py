# app/main.py
import os
from fastapi import FastAPI
from app.models import QuizSubmission
from app.quiz_data import QUIZ
from app.db import init_db, save_result
from app.telegram import send_result_message
from typing import List

app = FastAPI(title="EDP Quiz API")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/quiz")
def get_quiz():
    safe_questions = []
    for q in QUIZ["questions"]:
        safe_questions.append({
            "id": q["id"],
            "text": q["text"],
            "choices": q["choices"]
        })
    return {"quiz_id": QUIZ["id"], "title": QUIZ["title"], "questions": safe_questions}

def compute_score(submission: QuizSubmission) -> int:
    answer_map = {q["id"]: q["answer"].upper() for q in QUIZ["questions"]}
    total = len(answer_map)
    correct = 0
    for a in submission.answers:
        correct_ans = answer_map.get(a.question_id)
        if not correct_ans:
            continue
        if a.answer.strip().upper() == correct_ans:
            correct += 1
    percent = round((correct / total) * 100) if total else 0
    return percent

@app.post("/submit")
async def submit_quiz(submission: QuizSubmission):
    percent = compute_score(submission)
    save_result(submission.student_name, submission.student_email, QUIZ["id"], percent, [a.dict() for a in submission.answers])
    try:
        await send_result_message(submission.student_name, QUIZ["title"], percent)
    except Exception as e:
        return {"message": "submitted", "percent": percent, "telegram_error": str(e)}
    return {"message": "submitted", "percent": percent}
