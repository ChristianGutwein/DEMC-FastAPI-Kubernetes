from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from app.schemas.schemas import TaxiZoneResponse
from app.services import taxi_metadata as metadata_handler
from sqlalchemy.orm import Session

from app.db.databricks_engine import get_session, session_for

from app.core.config import get_settings


_settings = get_settings()
SCHEMA = _settings.DATABRICKS_BRONZE_SCHEMA


router = APIRouter(prefix="/metadata", tags=["Taxi Trip Metadata"])



@router.get("/taxi_zones",
    response_model=List[TaxiZoneResponse],
    summary="Query taxi zones")
def list_zones(
    location_id: Optional[int] = Query(default=None, description="Filter by LocationID"),
    borough: Optional[str]     = Query(default=None, description="Filter by Borough"),
    zone: Optional[str]        = Query(default=None, description="Filter by Zone"),
    service_zone: Optional[str]= Query(default=None, description="Filter by Service Zone"),
    session: Session = Depends(session_for(schema=SCHEMA))):

    taxi_zones = metadata_handler.list_zones(location_id, borough, zone, service_zone, session)
    if not taxi_zones:
        raise HTTPException(status_code=404, detail="No Taxi zones found")
    return taxi_zones