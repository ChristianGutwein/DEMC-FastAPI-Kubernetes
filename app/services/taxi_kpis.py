
from fastapi import HTTPException
from sqlalchemy import func
from app.db.databricks_connector import fetch_all
from typing import Optional
from app.core.config import get_settings
from sqlalchemy.orm import Session
from app.db.databricks_engine import session_for
from app.models.data_table_objects import HourlyMetric, Trip
from app.schemas.schemas import GenericTaxiKPIsResponse


_settings = get_settings()
TABLE_NYC_TAXI_TRIPS_BY_HOUR = f"{_settings.DATABRICKS_CATALOG}.{_settings.DATABRICKS_GOLD_SCHEMA}.{_settings.DATABRICKS_TAXI_TRIPS_BY_HOUR}"

def get_trips_by_hour() -> Optional[dict]:
    query = f"SELECT * FROM {TABLE_NYC_TAXI_TRIPS_BY_HOUR} ORDER BY computation_timestamp DESC"
    return fetch_all(query)


def get_trips_by_hour_orm(session) -> Optional[dict]:
    query = session.query(HourlyMetric)
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No metrics found")
    return results


def get_generic_taxi_kpis(session) -> Optional[dict]:

    total_trips = session.query(func.count(Trip.uuid)).scalar()
    total_revenue = session.query(func.sum(Trip.total_amount)).scalar() or 0
    average_trip_distance = session.query(func.avg(Trip.trip_distance)).scalar() or 0
    average_fare = session.query(func.avg(Trip.fare_amount)).scalar() or 0
    average_tip = session.query(func.avg(Trip.tip_amount)).scalar() or 0

    return GenericTaxiKPIsResponse(
        total_trips=total_trips,
        total_revenue=total_revenue,
        average_trip_distance=average_trip_distance,
        average_fare=average_fare,
        average_tip=average_tip
    )