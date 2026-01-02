from sqlalchemy import String,TIMESTAMP,Integer
from src.models.base import UUIDModel, TimestampedModel
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.orm import Mapped, mapped_column

class Event(UUIDModel, TimestampedModel):
    activityName:Mapped[str] = mapped_column(String)
    description:Mapped[str] = mapped_column(String,nullable=True)
    startTime:Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))
    endTime:Mapped[datetime] = mapped_column(TIMESTAMP,nullable=True)
    