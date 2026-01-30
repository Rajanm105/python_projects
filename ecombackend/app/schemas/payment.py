from pydantic import BaseModel

class PaymentCreate(BaseModel):
    order_id: int

class PaymentResponse(BaseModel):
    id: int
    order_id: int
    gateway_order_id: str
    status: str

    class Config:
        from_attributes = True
