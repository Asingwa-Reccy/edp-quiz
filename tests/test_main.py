# tests/test_main.py
from app.models import QuizSubmission, AnswerItem
from app.main import compute_score

def test_compute_score_all_correct():
    answers = [AnswerItem(question_id="q1", answer="B"),
               AnswerItem(question_id="q2", answer="A"),
               AnswerItem(question_id="q3", answer="A")]
    submission = QuizSubmission(student_name="x", answers=answers)
    assert compute_score(submission) == 100

def test_compute_score_some_wrong():
    answers = [AnswerItem(question_id="q1", answer="A"),
               AnswerItem(question_id="q2", answer="A"),
               AnswerItem(question_id="q3", answer="C")]
    submission = QuizSubmission(student_name="x", answers=answers)
    # 1 out of 3 correct => 33 or 34 depending on rounding
    assert compute_score(submission) in (33, 34)
