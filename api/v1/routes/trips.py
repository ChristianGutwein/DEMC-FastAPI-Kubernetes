from fastapi import APIRouter, HTTPException, Query
from app.models.schemas import Trip, TripCreate, TripList, TripUpdate
from app.services.trips import list_trips, count_trips, get_trip, create_trip, update_trip, delete_trip


router = APIRouter(prefix="/trips", tags=["trips"])


@router.get("/", response_model=TripList)
async def get_trips(limit: int = Query(50, ge=1, le=500), offset: int = Query(0, ge=0)):
    total = count_trips()
    rows = list_trips(limit=limit, offset=offset)
    return {"total": total, "items": rows}


@router.get("/{trip_id}", response_model=Trip)
async def get_trip_by_id(trip_id: str):
    row = get_trip(trip_id)
    if not row:
        raise HTTPException(status_code=404, detail="Trip not found")
    return row


@router.post("/", response_model=Trip, status_code=201)
async def create_trip_endpoint(payload: TripCreate):
    row = create_trip(payload)
    return row


@router.put("/{trip_id}", response_model=Trip)
async def update_trip_endpoint(trip_id: str, payload: TripUpdate):
    row = update_trip(trip_id=trip_id, payload=payload)
    if not row:
        raise HTTPException(status_code=404, detail="Trip not found")
    return row


@router.delete("/{trip_id}", status_code=204)
async def delete_trip_endpoint(trip_id: str):
    ok = delete_trip(trip_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Trip not found")
    return None