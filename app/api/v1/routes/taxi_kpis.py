from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.schemas import HourlyMetricResponse
from app.services import taxi_kpis as kpi_handler
from sqlalchemy.orm import Session
from app.db.databricks_engine import session_for

from app.core.config import get_settings


_settings = get_settings()
SCHEMA = _settings.DATABRICKS_GOLD_SCHEMA


router = APIRouter(prefix="/kpis", tags=["Taxi Trip KPI's"])

#todo: add one further kpi endpoint with internal (own) logic using ORM models

@router.get("/trips_by_hour",
    response_model=List[HourlyMetricResponse])
def get_trips_by_hour():
    trips_by_hour = kpi_handler.get_trips_by_hour()
    if not trips_by_hour:
        raise HTTPException(status_code=404, detail="No data found")
    return trips_by_hour


@router.get("/trips_by_hour_orm",
    response_model=List[HourlyMetricResponse])
def get_trips_by_hour(session: Session = Depends(session_for(schema=SCHEMA))):
    trips_by_hour = kpi_handler.get_trips_by_hour()
    if not trips_by_hour:
        raise HTTPException(status_code=404, detail="No data found")
    return trips_by_hour