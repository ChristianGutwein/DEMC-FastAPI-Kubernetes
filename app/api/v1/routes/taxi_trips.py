from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.schemas import (
    TaxiTripCreateRequest,
    TaxiTripUpdateRequest,
    TaxiTripResponse,
)
from app.services import taxi_trips as taxi_data_handler
from app.core.security import get_api_key


router = APIRouter(prefix="/trips", tags=["Taxi Trips"], dependencies=[Depends(get_api_key)])

#todo: add pagination endpoint using ORM Model and filter options (in addition filter locations via text)!


@router.post("/", response_model=TaxiTripResponse)
def create_trip(trip: TaxiTripCreateRequest):
    return taxi_data_handler.create_trip(trip)


@router.get("/{uuid}", response_model=TaxiTripResponse)
def get_trip(uuid: str):
    trip = taxi_data_handler.get_trip(uuid)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip


@router.get("/", response_model=List[TaxiTripResponse])
def list_trips(limit: int = 10):
    return taxi_data_handler.list_trips(limit)

# @router.get("/paginated_list", response_model=List[TaxiTripResponse])
# def list_trips(limit: int = 10):
#     return taxi_data_handler.list_trips(limit)


@router.put("/{uuid}", response_model=TaxiTripResponse)
def update_trip(uuid: str, trip: TaxiTripUpdateRequest):
    updated = taxi_data_handler.update_trip(uuid, trip)
    if not updated:
        raise HTTPException(status_code=404, detail="Trip not found or no fields updated")
    return updated


@router.delete("/{uuid}")
def delete_trip(uuid: str):
    success = taxi_data_handler.delete_trip(uuid)
    if not success:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {"message": "Trip deleted"}