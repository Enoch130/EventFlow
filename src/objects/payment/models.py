from sqlalchemy import String,Integer
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

class Payment(UUIDModel, TimestampedModel):
    amount:Mapped[int] = mapped_column(Integer)
    paymentStatus:Mapped[str] = mapped_column(String)