from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payment(BaseModel):
    amount: float

@app.post("/pay")
def process_payment(payment: Payment):
    return {
        "message": "Payment processed successfully",
        "amount": payment.amount
    }