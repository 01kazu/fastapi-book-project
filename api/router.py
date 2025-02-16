from fastapi import APIRouter

import api
from api.routes import books, integration_conf

api_router = APIRouter()
api_router.include_router(integration_conf.router, prefix="", tags=["integration"] )
api_router.include_router(books.router, prefix="/books", tags=["books"])
