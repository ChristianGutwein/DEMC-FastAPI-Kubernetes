from fastapi import APIRouter, HTTPException
from typing import List
from app.models.schemas import (
    TaxiTripCreateRequest,
    TaxiTripUpdateRequest,
    TaxiTripResponse,
)
from app.services import taxi_metadata as metadata_handler


router = APIRouter(prefix="/metadata", tags=["Taxi Trip Metadata"])


@router.get("/{uuid}", response_model=TaxiTripResponse)
def get_trip(uuid: str):
    trip = metadata_handler.get_trip(uuid)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip