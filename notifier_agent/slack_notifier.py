import os
import requests
from dotenv import load_dotenv

load_dotenv()


def send_slack_notification(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    if not webhook_url:
        print("⚠️ SLACK_WEBHOOK_URL not configured.")
        return

    payload = {
        "text": message
    }

    response = requests.post(
        webhook_url,
        json=payload
    )

    if response.status_code == 200:
        print("📨 Slack notification sent successfully.")
    else:
        print(f"❌ Slack notification failed: {response.status_code}")