# app/quiz_data.py
from typing import List, Dict

QUIZ = {
    "title": "Event Driven Programming (EDP) - Short Quiz",
    "id": "edp-001",
    "questions": [
        {
            "id": "q1",
            "text": "What is the main idea of event-driven programming?",
            "choices": ["A) Write linear code", "B) React to events", "C) Use only synchronous IO", "D) Avoid functions"],
            "answer": "B"
        },
        {
            "id": "q2",
            "text": "Which of these is an example of an 'event'?",
            "choices": ["A) Timer fires", "B) Function declaration", "C) Variable assignment", "D) Compiler error"],
            "answer": "A"
        },
        {
            "id": "q3",
            "text": "In an event loop, what handles events?",
            "choices": ["A) Event listeners/handlers", "B) Database only", "C) The compiler", "D) CSS files"],
            "answer": "A"
        }
    ]
}
