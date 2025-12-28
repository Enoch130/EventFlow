from sqlalchemy import String,Datetime,Integer
from src.models.base import UUIDModel, TimestampedModel
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

class Event(UUIDModel, TimestampedModel):
    title:Mapped[str] = mapped_column(String, nullable=False)
    eventtype:Mapped[str] = mapped_column(String, nullable=False)
    description:Mapped[str] = mapped_column(String,nullable=True)
    location:Mapped[str] = mapped_column(String,nullable=False)
    locationaddress:Mapped[str] = mapped_column(String, nullable=True) 
    eventdate:Mapped[str] = mapped_column(Datetime,nullable=False) #am i supposed to us Datetime or datetime
    deadlinedate:Mapped[str] = mapped_column(Datetime,nullable=True)
    capacity:Mapped[int] = mapped_column(Integer,nullable=False)
    guestaccompany:Mapped[int] = mapped_column(Integer,nullable=True) # is there a way i can prevent a user from bring more a specific number
    status:Mapped[str] = mapped_column(String,nullable=False)
    additionaldetails:Mapped[str] = mapped_column(String, nullable=True) 
    image:Mapped[str] = mapped_column(String,nullable=True)
