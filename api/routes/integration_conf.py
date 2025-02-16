from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.config import settings

router = APIRouter()

integration_json = {
  "data": {
    "date": {
      "created_at": "2025-02-15",
      "updated_at": "2025-02-15"
    },
    "descriptions": {
      "app_name": "telex-ci-cd",
      "app_description": "ci/cd notification app",
      "app_logo": "http://16.171.129.130",
      "app_url": "http://16.171.129.130",
      "background_color": "#fff"
    },
    "is_active": True,
    "integration_type": "modifier", # changed this
    "key_features": [
      "realtime-updates",
      "click notifications"
    ],
    "author": "Joshua",
    "settings": [
      {
        "label": "slack-channel",
        "type": "text",
        "required": True,
        "default": "#DevopsAlert"
      },
      {
        "label": "time interval",
        "type": "dropdown",
        "required": True,
        "default": "immediate",
        "options": [
          "immediate",
          "every 5 mins",
          "every 10 mins",
          "every 1 hour"
        ]
      },
      {
        "label": "event type",
        "type": "dropdown",
        "required": True,
        "default": "ci_pipeline",
        "options": [
          "ci_pipeline",
          "cd_pipeline",
          "deployment",
          "error"
        ]
      },
      {
        "label": "message",
        "type": "text",
        "required": True,
        "default": "Basic"
      },
      {
        "label": "include logs",
        "type": "checkbox",
        "required": True,
        "default": "true"
      }
    ],
    "target_url": settings.SLACK_WEBHOOK_URL,
    "tick_url": settings.TICK_URL
  }
}

@router.get('/integration-config')
async def get_integration_json():
    return JSONResponse(content=integration_json)