# models.py
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, BigInteger, Float, String, DateTime, Numeric

class Base(DeclarativeBase):
    pass

class TaxiZone(Base):
    __tablename__ = "taxi_zone_lookup"
    LocationID: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    Borough: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    Zone: Mapped[str] = mapped_column(String(200), index=True, nullable=False)
    service_zone: Mapped[str] = mapped_column(String(100), index=True, nullable=False)





class HourlyMetric(Base):
    __tablename__ = "kpi_trips_by_hour"  
    hour_of_day: Mapped[int] = mapped_column(Integer, primary_key=True)
    day_type: Mapped[str] = mapped_column(String(30), primary_key=True)         
    peak_status: Mapped[str] = mapped_column(String(30), primary_key=True)      
    computation_timestamp: Mapped[DateTime] = mapped_column(DateTime, primary_key=True)

    total_trips: Mapped[int] = mapped_column(BigInteger, nullable=False)
    total_revenue: Mapped[float] = mapped_column(Float, nullable=False)
    avg_fare: Mapped[float] = mapped_column(Float, nullable=False)
    avg_distance: Mapped[float] = mapped_column(Float, nullable=False)
    avg_duration: Mapped[float] = mapped_column(Float, nullable=False)
    avg_tip_percentage: Mapped[float] = mapped_column(Numeric(11, 2), nullable=False)
