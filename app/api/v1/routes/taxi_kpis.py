from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.schemas import (
    TaxiTripCreateRequest,
    TaxiTripUpdateRequest,
    TaxiTripResponse,
)
from app.services import taxi_kpis as kpi_handler


router = APIRouter(prefix="/kpis", tags=["Taxi Trip KPI's"])