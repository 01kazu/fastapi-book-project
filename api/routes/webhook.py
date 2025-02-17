from fastapi import APIRouter, Request
import httpx
import logging
from core.config import settings

router = APIRouter()

logging.basicConfig(level=logging.INFO)

@router.post("/telex-webhook")
async def telex_to_slack(request: Request):
    try:
        payload = await request.json()
        logging.info(f"Received data from Telex: {payload}")

        event_name = payload.get("event_name", "ci_pipeline")
        username = payload.get("username", "Telex Bot")
        status = payload.get("status", "info")
        message = payload.get("message", "No message provided.")

        slack_webhook_url = settings.SLACK_WEBHOOK_URL
        
        event_mapping = {
            "ci_pipeline": "🛠️ CI Pipeline",
            "cd_pipeline": "🚀 CD Pipeline"
        }
        event_display = event_mapping.get(event_name, event_name)

        slack_message = {
            "text": f"*{event_display}* - {status.upper()} 🚀\n\n_{username}_:\n>{message}"
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(slack_webhook_url, json=slack_message)
            response.raise_for_status()

        logging.info("Notification sent to Slack successfully!")
        return {"status": "success", "message": "Notification sent to Slack."}

    except Exception as e:
        logging.error(f"Error forwarding to Slack: {str(e)}")
        return {"status": "error", "message": str(e)}
