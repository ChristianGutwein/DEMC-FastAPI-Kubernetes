from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from decimal import Decimal


# ---------- CREATE ----------
class TaxiTripCreateRequest(BaseModel):
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
    pickup_location_id: Optional[int]
    dropoff_location_id: Optional[int]
    store_and_forward: Optional[bool]


# ---------- UPDATE ----------
class TaxiTripUpdateRequest(BaseModel):
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
    pickup_location_id: Optional[int]
    dropoff_location_id: Optional[int]
    store_and_forward: Optional[bool]


# ---------- RESPONSE ----------
class TaxiTripResponse(BaseModel):
    uuid: Optional[str]
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
    pickup_location_id: Optional[int]
    dropoff_location_id: Optional[int]
    store_and_forward: Optional[bool]

    model_config = ConfigDict(from_attributes=True)



class TaxiZoneResponse(BaseModel):
    LocationID: int
    Borough: str
    Zone: str
    service_zone: str

    model_config = ConfigDict(from_attributes=True)



class HourlyMetricResponse(BaseModel):
    hour_of_day: int
    total_trips: int
    total_revenue: float
    avg_fare: float
    avg_distance: float
    avg_duration: float
    avg_tip_percentage: Decimal
    peak_status: str
    day_type: str
    computation_timestamp: datetime
    
    model_config = ConfigDict(from_attributes=True)