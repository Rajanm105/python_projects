from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
