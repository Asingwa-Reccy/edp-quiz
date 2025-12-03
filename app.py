# app/db.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "results.db"

def init_db():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        student_email TEXT,
        quiz_id TEXT,
        percent INTEGER,
        raw_answers TEXT,
        ts DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    con.commit()
    con.close()

def save_result(student_name, student_email, quiz_id, percent, raw_answers):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("INSERT INTO results (student_name, student_email, quiz_id, percent, raw_answers) VALUES (?,?,?,?,?)",
                (student_name, student_email, quiz_id, percent, str(raw_answers)))
    con.commit()
    con.close()
