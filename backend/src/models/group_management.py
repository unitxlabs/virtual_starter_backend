from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy import TIMESTAMP, Column, DateTime, Integer, String
from src.db.database_init import Base


class Group(Base):
    __tablename__ = "group_management"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    production_line = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(datetime.timezone.utc + 8))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(datetime.timezone.utc + 8),
        onupdate=lambda: datetime.now(datetime.timezone.utc + 8),
    )


class GroupCreate(BaseModel):
    name: str
    production_line: Optional[str] = None


class GroupDelete(BaseModel):
    id: int
