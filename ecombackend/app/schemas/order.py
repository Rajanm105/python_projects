from pydantic import BaseModel
from typing import List

class OrderCreate(BaseModel):
    total_amount: float

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str

    class Config:
        from_attributes = True
