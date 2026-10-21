import os
import requests
from dotenv import load_dotenv

# .env file se values load karna
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()


if __name__ == "__main__":
    result = send_telegram_alert("🚨 ML Canary Test Alert! Agar ye message mila, matlab sab sahi connect hai.")
    print(result)