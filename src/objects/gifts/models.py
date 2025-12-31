from sqlalchemy import String,Integer
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

class Gifts(UUIDModel, TimestampedModel):
    guestName:Mapped[str] = mapped_column(String)
    amount:Mapped[int] = mapped_column(Integer,nullable=True)
    paymentMethod:Mapped[str] = mapped_column(String)
    paymentStatus:Mapped[str] = mapped_column(String)