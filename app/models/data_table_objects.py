# models.py
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, BigInteger, Float, String, DateTime, Numeric, Column, Boolean

class Base(DeclarativeBase):
    pass

class Trip(Base):
    __tablename__ = 'nyc_taxi_cleaned'
    uuid = Column(String, primary_key=True, index=True)
    passenger_count = Column(Integer)
    trip_distance = Column(Float)
    store_and_fwd_flag = Column(String(1))
    payment_type = Column(Integer)
    fare_amount = Column(Float)
    extra = Column(Float)
    mta_tax = Column(Float)
    tip_amount = Column(Float)
    tolls_amount = Column(Float)
    improvement_surcharge = Column(Float)
    total_amount = Column(Float)
    congestion_surcharge = Column(Float)
    airport_fee = Column(Float)
    pickup_datetime = Column(DateTime, nullable=False)
    dropoff_datetime = Column(DateTime, nullable=False)
    vendor_id = Column(Integer)
    rate_code_id = Column(Integer)
    pickup_location_id = Column(Integer)
    dropoff_location_id = Column(Integer)
    store_and_forward = Column(Boolean)
    trip_duration = Column(Float)
    fare_per_mile = Column(Float)
    tip_percentage = Column(Float)
    pickup_hour = Column(Integer)
    pickup_day = Column(Integer)
    pickup_month = Column(Integer)
    is_weekend = Column(Boolean)
    is_peak_hour = Column(Boolean)
    payment_type_desc = Column(String(50))
    rate_code_desc = Column(String(50))
    avg_speed = Column(Float)


class TaxiZone(Base):
    __tablename__ = "taxi_zone_lookup"
    LocationID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Borough: Mapped[str] = mapped_column(String(100))
    Zone: Mapped[str] = mapped_column(String(200))
    service_zone: Mapped[str] = mapped_column(String(100))


class HourlyMetric(Base):
    __tablename__ = "kpi_trips_by_hour"  
    hour_of_day = Column(Integer, primary_key=True)
    day_type = Column(String(30), primary_key=True)         
    peak_status = Column(String(30), primary_key=True)      
    computation_timestamp = Column(DateTime)

    total_trips = Column(BigInteger)
    total_revenue = Column(Float)
    avg_fare = Column(Float)
    avg_distance = Column(Float)
    avg_duration = Column(Float)
    avg_tip_percentage = Column(Numeric(11, 2))
