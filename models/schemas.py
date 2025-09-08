from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class NYCTaxiEnriched(BaseModel):
    dropoff_location_id: Optional[int]
    pickup_location_id: Optional[int]
    passenger_count: Optional[int]
    trip_distance: Optional[float]
    store_and_fwd_flag: Optional[str]
    payment_type: Optional[int]
    fare_amount: Optional[float]
    extra: Optional[float]
    mta_tax: Optional[float]
    tip_amount: Optional[float]
    tolls_amount: Optional[float]
    improvement_surcharge: Optional[float]
    total_amount: Optional[float]
    congestion_surcharge: Optional[float]
    airport_fee: Optional[float]
    pickup_datetime: Optional[datetime]
    dropoff_datetime: Optional[datetime]
    vendor_id: Optional[str]
    rate_code_id: Optional[int]
    store_and_forward: Optional[bool]

    class Config:
        extra = "forbid"  # prevent extra fields


class TripCreate(NYCTaxiEnriched):
    trip_id: str


class TripUpdate(NYCTaxiEnriched):
    pass


class Trip(NYCTaxiEnriched):
    trip_id: str = Field(..., description="Primärschlüssel (string)")


class TripList(BaseModel):
    total: int
    items: list[Trip]