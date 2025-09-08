from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from app.schemas.schemas import TaxiZoneResponse
from app.services import taxi_metadata as metadata_handler
from sqlalchemy.orm import Session

from db.databricks_engine import get_session

from app.core.config import get_settings


_settings = get_settings()
SCHEMA = _settings.DATABRICKS_BRONZE_SCHEMA


router = APIRouter(prefix="/metadata", tags=["Taxi Trip Metadata"])



@router.get("/taxi_zones",
    response_model=List[TaxiZoneResponse],
    summary="Query taxi zones (sync)")
def list_zones(
    location_id: Optional[int],
    borough: Optional[str],
    zone: Optional[str],
    service_zone: Optional[str],
    session: Session = Depends(get_session(schema=SCHEMA))):

    trip = metadata_handler.list_zones(location_id, borough, zone, service_zone, session)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip