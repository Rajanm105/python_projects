from pydantic import BaseModel

class CartAdd(BaseModel):
    product_id: int
    quantity: int = 1

class CartUpdate(BaseModel):
    quantity: int

class CartItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True
