from datetime import datetime

from sqlalchemy import JSON, Column, DateTime, Integer, String
from pydantic import BaseModel
from typing import Optional
from backend.src.db.database_init import Base


class DeviceManagement(Base):
    __tablename__ = 'device_management'

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String(50), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    type = Column(Integer, nullable=False)  # 1=相机，2=控制器，3=PLC
    group_id = Column(Integer, nullable=True)
    production_line_id = Column(Integer, nullable=True)
    workstation_id = Column(Integer, nullable=True)
    config = Column(JSON, nullable=True)
    status = Column(Integer, default=0)  # 0=离线，1=在线
    created_at = Column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(datetime.timezone.utc),
        onupdate=lambda: datetime.now(datetime.timezone.utc),
    )

    def __repr__(self):
        return f"<DeviceManagement(device_id='{self.device_id}', name='{self.name}', type={self.type}, status={self.status})>"


class DeviceManagementBase(BaseModel):
    device_id: str
    name: str
    type: int
    group_id: Optional[int] = None
    production_line_id: Optional[int] = None
    workstation_id: Optional[int] = None
    config: Optional[dict] = None
    status: int


class DeviceManagementCreate(DeviceManagementBase):
    pass


class DeviceManagementUpdate(DeviceManagementBase):
    pass


class DeviceManagementInDB(DeviceManagementBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
