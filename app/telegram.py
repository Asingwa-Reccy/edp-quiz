# app/telegram.py
import os
import httpx
from dotenv import load_dotenv

load_dotenv()  # load .env when running in Codespace

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # e.g. "@my_channel" or -1001234567890

async def send_result_message(student_name: str, quiz_title: str, percent: int):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        raise RuntimeError("Telegram token or chat id not configured in env")
    text = f"{student_name} has finished the quiz {quiz_title} with result {percent}%"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text})
        resp.raise_for_status()
        return resp.json()
