import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    product_id : int
    quantity: int

orders_db = []

@app.post("/order")
def create_order(order: Order):
    res = requests.get(f"http://localhost:8002/product/{order.product_id}")

    if res.status_code != 200:
        raise HTTPException(status_code=400, detail="Unable to fetch product")

    product = res.json()

    if "stock" not in product:
        raise HTTPException(status_code=400, detail="Product data invalid")

    if product["stock"] < order.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock available")
    
    orders_db.append(order.dict())
    return {"message": "Order created successfully"}