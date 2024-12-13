from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.db.database_init import Base, engine, get_db
from src.models.device_management import (
    DeviceManagement,
    DeviceManagementCreate,
    DeviceManagementInDB,
    DeviceManagementUpdate,
)


# Initialize the API router
router = APIRouter()


# CRUD operations
@router.post("/devices/", response_model=DeviceManagementInDB)
def create_device(device: DeviceManagementCreate, db: Session = Depends(get_db)):
    db_device = DeviceManagement(**device.model_dump())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


@router.get("/devices/", response_model=List[DeviceManagementInDB])
def read_devices(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    devices = db.query(DeviceManagement).offset(skip).limit(limit).all()
    return devices


@router.get("/devices/{device_id}", response_model=DeviceManagementInDB)
def read_device(device_id: int, db: Session = Depends(get_db)):
    device = db.query(DeviceManagement).filter(DeviceManagement.id == device_id).first()
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@router.put("/devices/{device_id}", response_model=DeviceManagementInDB)
def update_device(device_id: int, device: DeviceManagementUpdate, db: Session = Depends(get_db)):
    db_device = db.query(DeviceManagement).filter(DeviceManagement.id == device_id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    for key, value in device.model_dump().items():
        setattr(db_device, key, value)
    db.commit()
    db.refresh(db_device)
    return db_device


@router.delete("/devices/{device_id}", response_model=DeviceManagementInDB)
def delete_device(device_id: int, db: Session = Depends(get_db)):
    db_device = db.query(DeviceManagement).filter(DeviceManagement.id == device_id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    db.delete(db_device)
    db.commit()
    return db_device
