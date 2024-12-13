from typing import List

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from backend.src.api.group_management import Group, GroupCreate, GroupDelete
from src.db.database_init import get_db

app = FastAPI()
router = APIRouter()


@router.get("/group/query", response_model=List[Group])
def query_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    groups = db.query(Group).offset(skip).limit(limit).all()
    return groups


@router.post("/group/create", response_model=GroupCreate)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    db_group = Group(name=group.name, production_line=group.production_line)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


@router.post("/group/delete")
def delete_group(group: GroupDelete, db: Session = Depends(get_db)):
    db_group = db.query(Group).filter(Group.id == group.id).first()
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    db.delete(db_group)
    db.commit()
    return {"detail": "Group deleted"}
