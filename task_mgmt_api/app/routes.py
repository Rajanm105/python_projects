from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User, Task
from app.schemas import UserCreate, TaskCreate
from app.auth import hash_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(email=user.email, password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    return {"message": "User created"}

@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(title=task.title, owner_id=1)
    db.add(new_task)
    db.commit()
    return {"message": "Task created"}
