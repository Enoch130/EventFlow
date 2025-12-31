from sqlalchemy import String,Integer
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

class Vendors(UUIDModel, TimestampedModel):
    name:Mapped[str] = mapped_column(String)
    category:Mapped[str] = mapped_column(String)
    status:Mapped[str] = mapped_column(String)
    email:Mapped[str] = mapped_column(String,unique=True, index = True)
    phoneNumber:Mapped[str] = mapped_column(String,nullable=True)