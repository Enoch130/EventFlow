from sqlalchemy import String
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

class User(UUIDModel, TimestampedModel):
    name:Mapped[str] = mapped_column(String)
    email:Mapped[str] = mapped_column(String,unique=True, index = True)
    phoneNumber:Mapped[str] = mapped_column(String,nullable=True)
    message:Mapped[str] = mapped_column(String)
    invitationStatus:Mapped[str] = mapped_column(String)