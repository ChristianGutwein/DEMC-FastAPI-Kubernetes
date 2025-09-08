from fastapi import FastAPI
from loguru import logger
from app.core.config import get_settings
from app.api.v1.routes.trips import router as trips_router


S = get_settings()

app = FastAPI(title=S.APP_NAME, debug=S.APP_DEBUG)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "env": S.APP_ENV}

app.include_router(trips_router, prefix="/api/v1")