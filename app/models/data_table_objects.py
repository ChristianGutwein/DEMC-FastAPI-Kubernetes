# models.py
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer

class Base(DeclarativeBase):
    pass

class TaxiZone(Base):
    __tablename__ = "taxi_zone_lookup"
    LocationID: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    Borough: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    Zone: Mapped[str] = mapped_column(String(200), index=True, nullable=False)
    service_zone: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
