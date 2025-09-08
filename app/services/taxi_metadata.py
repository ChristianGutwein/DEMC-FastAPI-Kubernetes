from fastapi import FastAPI, Depends, Query
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.data_table_objects import TaxiZone



def list_zones(
    location_id: Optional[int],
    borough: Optional[str],
    zone: Optional[str],
    service_zone: Optional[str],
    session: Session
):
    stmt = select(TaxiZone)
    if location_id is not None:
        stmt = stmt.where(TaxiZone.LocationID == location_id)
    if borough is not None:
        stmt = stmt.where(TaxiZone.Borough.like(f"%{borough}%"))
    if zone is not None:
        stmt = stmt.where(TaxiZone.Zone.like(f"%{zone}%"))
    if service_zone is not None:
        stmt = stmt.where(TaxiZone.service_zone.like(f"%{service_zone}%"))
    stmt = stmt.order_by(TaxiZone.LocationID)
    result = session.execute(stmt)
    return result.scalars().all()
