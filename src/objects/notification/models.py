from sqlalchemy import String
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

class Notification(UUIDModel, TimestampedModel):
    notificationType:Mapped[str] = mapped_column(String)
    message:Mapped[str] = mapped_column(String)
    status:Mapped[str] = mapped_column(String)