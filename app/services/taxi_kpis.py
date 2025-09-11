
from app.db.databricks_connector import fetch_all
from typing import Optional
from app.core.config import get_settings

_settings = get_settings()
TABLE_NYC_TAXI_TRIPS_BY_HOUR = f"{_settings.DATABRICKS_CATALOG}.{_settings.DATABRICKS_GOLD_SCHEMA}.{_settings.DATABRICKS_TAXI_TRIPS_BY_HOUR}"

def get_trips_by_hour() -> Optional[dict]:
    query = f"SELECT * FROM {TABLE_NYC_TAXI_TRIPS_BY_HOUR} ORDER BY computation_timestamp DESC"
    return fetch_all(query)

#todo: use also ORM method