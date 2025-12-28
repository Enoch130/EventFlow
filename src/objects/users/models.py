from sqlalchemy import String
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

class User(UUIDModel, TimestampedModel):
    firstname:Mapped[str] = mapped_column(String, nullable=False)
    middlename:Mapped[str] = mapped_column(String, nullable=True)
    lastname:Mapped[str] = mapped_column(String, nullable=False)
    email:Mapped[str] = mapped_column(String,unique=True, index = True)
    phonenumber:Mapped[str] = mapped_column(String,nullable=True)
    password:Mapped[str] = mapped_column(String,nullable=False)
    role:Mapped[str] = mapped_column(String, nullable=False) # is there alternative to give options