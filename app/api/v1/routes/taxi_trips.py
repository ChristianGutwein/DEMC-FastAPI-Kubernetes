from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.schemas import (
    TaxiTripCreateRequest,
    TaxiTripUpdateRequest,
    TaxiTripResponse,
)
from app.services import taxi_trips as taxi_data_handler
from sqlalchemy.orm import Session
from app.db.databricks_engine import session_for

from app.core.config import get_settings
from app.core.security import get_api_key


router = APIRouter(prefix="/trips", tags=["Taxi Trips"], dependencies=[Depends(get_api_key)])


_settings = get_settings()
SCHEMA = _settings.DATABRICKS_SILVER_SCHEMA


@router.post("/", response_model=TaxiTripResponse)
def create_trip(trip: TaxiTripCreateRequest):
    return taxi_data_handler.create_trip(trip)

#todo: ensure that uuid is created in data table or add techn. id (also needed for clean pagination e.g.), copy taxi_zone_lookup into silver layer?
#todo: how to ensure/validate inputs like pick up & drop off locations (should be in lookup table) and values like f or n. (only addition / on top task!)

@router.post("/orm", response_model=TaxiTripResponse)
def create_trip_orm(trip: TaxiTripCreateRequest, session: Session = Depends(session_for(schema=SCHEMA))):
    return taxi_data_handler.create_trip_orm(trip, session)


@router.get("/{uuid}", response_model=TaxiTripResponse)
def get_trip(uuid: str):
    trip = taxi_data_handler.get_trip(uuid)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip


@router.get("/", response_model=List[TaxiTripResponse])
def list_trips(limit: int = 10):
    return taxi_data_handler.list_trips(limit)

#to do: add orm method

#todo: add pagination endpoint using ORM Model (or sql solution) with filter and sorting options (in addition filter locations via text from lookup table)!



@router.put("/{uuid}", response_model=TaxiTripResponse)
def update_trip(uuid: str, trip_update: TaxiTripUpdateRequest):
    updated = taxi_data_handler.update_trip(uuid, trip_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Trip not found or no fields updated")
    return updated

#to do: add orm method and use patch endpoint 
@router.patch("/{uuid}")
def update_trip(uuid: str, trip_update: TaxiTripUpdateRequest, session: Session = Depends(session_for(schema=SCHEMA))):
    updated = taxi_data_handler.update_trip_orm(uuid, trip_update, session)
    if not updated:
        raise HTTPException(status_code=404, detail="Trip not found or no fields updated")
    return updated


@router.delete("/{uuid}")
def delete_trip(uuid: str):
    success = taxi_data_handler.delete_trip(uuid)
    if not success:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {"message": "Trip deleted"}