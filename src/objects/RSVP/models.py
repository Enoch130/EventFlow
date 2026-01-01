from sqlalchemy import String
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

class User(UUIDModel, TimestampedModel):
    response:Mapped[str] = mapped_column(String)
    