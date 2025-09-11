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
    trip_duration: Optional[float]
    fare_per_mile: Optional[float]
    tip_percentage: Optional[float]
    pickup_hour: Optional[int]
    pickup_day: Optional[int]
    pickup_month: Optional[int]
    is_weekend: Optional[int]
    is_peak_hour: Optional[int]
    payment_type_desc: Optional[str]
    rate_code_desc: Optional[str]
    avg_speed: Optional[float]

    
# ---------- UPDATE ----------
class TaxiTripUpdateRequest(BaseModel):
    passenger_count: Optional[int] = None
    trip_distance: Optional[float] = None
    store_and_fwd_flag: Optional[str] = None
    payment_type: Optional[int] = None
    fare_amount: Optional[float] = None
    extra: Optional[float] = None
    mta_tax: Optional[float] = None
    tip_amount: Optional[float] = None
    tolls_amount: Optional[float] = None
    improvement_surcharge: Optional[float] = None
    total_amount: Optional[float] = None
    congestion_surcharge: Optional[float] = None
    airport_fee: Optional[float] = None
    pickup_datetime: Optional[datetime] = None   # <-- changed
    dropoff_datetime: Optional[datetime] = None  # <-- changed
    vendor_id: Optional[int] = None
    rate_code_id: Optional[int] = None
    pickup_location_id: Optional[int] = None
    dropoff_location_id: Optional[int] = None
    store_and_forward: Optional[bool] = None
    trip_duration: Optional[float] = None
    fare_per_mile: Optional[float] = None
    tip_percentage: Optional[float] = None
    pickup_hour: Optional[int] = None
    pickup_day: Optional[int] = None
    pickup_month: Optional[int] = None
    is_weekend: Optional[bool] = None
    is_peak_hour: Optional[bool] = None
    payment_type_desc: Optional[str] = None
    rate_code_desc: Optional[str] = None
    avg_speed: Optional[float] = None



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
    trip_duration: Optional[float]
    fare_per_mile: Optional[float]
    tip_percentage: Optional[float]
    pickup_hour: Optional[int]
    pickup_day: Optional[int]
    pickup_month: Optional[int]
    is_weekend: Optional[int]
    is_peak_hour: Optional[int]
    payment_type_desc: Optional[str]
    rate_code_desc: Optional[str]
    avg_speed: Optional[float]

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


class GenericTaxiKPIsResponse(BaseModel):
    total_trips: int
    total_revenue: float
    average_trip_distance: float
    average_fare: float
    average_tip: float

    model_config = ConfigDict(from_attributes=True)