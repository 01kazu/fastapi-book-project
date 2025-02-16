from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router
from api.router.integration_conf import router as integration_route
from api.routes import integration_conf
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Integration router
app.include_router(integration_conf)
app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}


@app.get("/telex-webhook")
async def telex_webhook() -> None:
    return {'response': {'detail': 'It works'}}

