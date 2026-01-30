from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User, Note
from app.schemas import UserCreate, NoteCreate
from app.auth import hash_password, verify_password, create_token, decode_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(authorization: str = Header(...)):
    token = authorization.split(" ")[1]
    payload = decode_token(token)
    return payload["user_id"]

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    u = User(email=user.email, password=hash_password(user.password))
    db.add(u)
    db.commit()
    return {"msg": "user created"}

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    u = db.query(User).filter(User.email == user.email).first()
    if not u or not verify_password(user.password, u.password):
        return {"error": "invalid creds"}
    return {"token": create_token(u.id)}

@router.post("/notes")
def create_note(note: NoteCreate, user_id=Depends(get_current_user), db: Session = Depends(get_db)):
    n = Note(content=note.content, owner_id=user_id)
    db.add(n)
    db.commit()
    return {"msg": "note created"}

# 🚨 IDOR VULNERABILITY
@router.get("/notes/{note_id}")
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    return note

# Secured API
@router.get("/notes/{note_id}")
def get_note_secure(
    note_id: int,
    user_id=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    note = db.query(Note).filter(
        Note.id == note_id,
        Note.owner_id == user_id
    ).first()

    if not note:
        return {"error": "not found or forbidden"}

    return note