# app/models.py

from pydantic import BaseModel

# This class describes the information we will receive
# when a student finishes a quiz.
class QuizResult(BaseModel):
    student_name: str   # Example: "Joe Doe"
    quiz_name: str      # Example: "EDP"
    score: int          # Example: 80
