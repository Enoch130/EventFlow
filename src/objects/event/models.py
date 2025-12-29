from sqlalchemy import String,TIMESTAMP,Integer
from src.models.base import UUIDModel, TimestampedModel
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.orm import Mapped, mapped_column

class Event(UUIDModel, TimestampedModel):
    title:Mapped[str] = mapped_column(String)
    eventType:Mapped[str] = mapped_column(String)
    description:Mapped[str] = mapped_column(String,nullable=True)
    location:Mapped[str] = mapped_column(String)
    locationAddress:Mapped[str] = mapped_column(String, nullable=True) 
    eventDate:Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))
    deadlineDate:Mapped[datetime] = mapped_column(TIMESTAMP,nullable=True)
    capacity:Mapped[int] = mapped_column(Integer)
    guestAccompany:Mapped[int] = mapped_column(Integer,nullable=True) 
    status:Mapped[str] = mapped_column(String)
    additionalDetails:Mapped[str] = mapped_column(String, nullable=True) 
    image:Mapped[str] = mapped_column(String,nullable=True)
