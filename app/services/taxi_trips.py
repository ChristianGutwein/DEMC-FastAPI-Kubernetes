from app.core.config import get_settings
from typing import Optional
from app.db.databricks_connector import fetch_all, fetch_one, execute
from app.schemas.schemas import TaxiTripCreateRequest, TaxiTripUpdateRequest


_settings = get_settings()
TABLE_NYC_TAXI = f"{_settings.DATABRICKS_CATALOG}.{_settings.DATABRICKS_SILVER_SCHEMA}.{_settings.DATABRICKS_TAXI_TABLE}"

#todo: add pagination endpoint and add sql model variant!

def create_trip(trip: TaxiTripCreateRequest) -> dict:
    fields = trip.dict()
    query = f"""
        INSERT INTO {TABLE_NYC_TAXI} ({", ".join(fields.keys())})
        VALUES ({", ".join(["?"] * len(fields))})
    """
    execute(query, tuple(fields.values()))
    # return the created row for consistency
    return get_trip(trip.uuid)


def get_trip(uuid: str) -> Optional[dict]:
    query = f"SELECT * FROM {TABLE_NYC_TAXI} WHERE uuid = ?"
    return fetch_one(query, (uuid,))


def list_trips(limit: int = 10) -> list[dict]:
    query = f"SELECT * FROM {TABLE_NYC_TAXI} ORDER BY pickup_datetime DESC LIMIT {limit}"
    return fetch_all(query)


def update_trip(uuid: str, trip: TaxiTripUpdateRequest) -> Optional[dict]:
    fields = {k: v for k, v in trip.dict().items() if v is not None}
    if not fields:
        return get_trip(uuid)  # nothing to update, return existing

    set_clause = ", ".join([f"{k} = ?" for k in fields.keys()])
    values = list(fields.values()) + [uuid]
    query = f"UPDATE {TABLE_NYC_TAXI} SET {set_clause} WHERE uuid = ?"
    rowcount = execute(query, tuple(values))

    if rowcount == 0:
        return None
    return get_trip(uuid)


def delete_trip(uuid: str) -> bool:
    query = f"DELETE FROM {TABLE_NYC_TAXI} WHERE uuid = ?"
    rowcount = execute(query, (uuid,))
    return rowcount > 0




# def count_trips() -> int:
#     row = fetch_one(f"SELECT COUNT(*) AS c FROM {TABLE_FQN}")
#     return int(row["c"]) if row else 0


# def list_trips(limit: int = 50, offset: int = 0):
#     rows = fetch_all(
#     f"""
#     SELECT *
#     FROM {TABLE_FQN}
#     ORDER BY pickup_datetime DESC
#     LIMIT ? OFFSET ?
#     """,
#     [limit, offset],
#     )
#     return rows



# def get_trip(trip_id: str) -> Optional[dict]:
#     return fetch_one(
#     f"SELECT * FROM {TABLE_FQN} WHERE trip_id = ?",
#     [trip_id],
#     )



# def create_trip(data: dict):
#     placeholders = ", ".join(["?"] * len(data))
#     columns = ", ".join(data.keys())
#     values = list(data.values())
#     execute(
#     f"INSERT INTO {TABLE_FQN} ({columns}) VALUES ({placeholders})",
#     values,
#     )
#     return get_trip(data["trip_id"])




# def update_trip(trip_id: str, data: dict):
#     set_clause = ", ".join([f"{k} = ?" for k in data.keys()])
#     values = list(data.values()) + [trip_id]
#     execute(
#     f"UPDATE {TABLE_FQN} SET {set_clause} WHERE trip_id = ?",
#     values,
#     )
#     return get_trip(trip_id)




# def delete_trip(trip_id: str) -> bool:
#     rc = execute(
#     f"DELETE FROM {TABLE_FQN} WHERE trip_id = ?",
#     [trip_id],
#     )
#     return rc != 0