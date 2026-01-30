from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class TaskCreate(BaseModel):
    title: str
