from fastapi import FastAPI
from loguru import logger
from app.core.config import get_settings
from app.api.v1.routes.taxi_trips import router as taxi_trips_router
from app.api.v1.routes.taxi_kpis import router as taxi_kpis_router
from app.api.v1.routes.taxi_metadata import router as taxi_metadata_router


_settings = get_settings()

app = FastAPI(title=_settings.APP_NAME, debug=_settings.APP_DEBUG)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "env": _settings.APP_ENV}

app.include_router(taxi_trips_router, prefix="/v1")
app.include_router(taxi_kpis_router, prefix="/v1")
app.include_router(taxi_metadata_router, prefix="/v1")