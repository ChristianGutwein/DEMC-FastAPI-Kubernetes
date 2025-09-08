from app.core.config import get_settings
from app.db.databricks import fetch_all, fetch_one, execute
from typing import Optional


S = get_settings()

TABLE_FQN = f"{S.DATABRICKS_CATALOG}.{S.DATABRICKS_SCHEMA}.{S.DATABRICKS_TABLE}"

def count_trips() -> int:
    row = fetch_one(f"SELECT COUNT(*) AS c FROM {TABLE_FQN}")
    return int(row["c"]) if row else 0


def list_trips(limit: int = 50, offset: int = 0):
    rows = fetch_all(
    f"""
    SELECT *
    FROM {TABLE_FQN}
    ORDER BY pickup_datetime DESC
    LIMIT ? OFFSET ?
    """,
    [limit, offset],
    )
    return rows



def get_trip(trip_id: str) -> Optional[dict]:
    return fetch_one(
    f"SELECT * FROM {TABLE_FQN} WHERE trip_id = ?",
    [trip_id],
    )



def create_trip(data: dict):
    placeholders = ", ".join(["?"] * len(data))
    columns = ", ".join(data.keys())
    values = list(data.values())
    execute(
    f"INSERT INTO {TABLE_FQN} ({columns}) VALUES ({placeholders})",
    values,
    )
    return get_trip(data["trip_id"])




def update_trip(trip_id: str, data: dict):
    set_clause = ", ".join([f"{k} = ?" for k in data.keys()])
    values = list(data.values()) + [trip_id]
    execute(
    f"UPDATE {TABLE_FQN} SET {set_clause} WHERE trip_id = ?",
    values,
    )
    return get_trip(trip_id)




def delete_trip(trip_id: str) -> bool:
    rc = execute(
    f"DELETE FROM {TABLE_FQN} WHERE trip_id = ?",
    [trip_id],
    )
    return rc != 0