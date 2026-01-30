from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentResponse
from app.auth.dependencies import get_current_user
from app.models.user import User
import uuid

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/create", response_model=PaymentResponse)
def create_payment(
    payload: PaymentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    payment = Payment(
        order_id=payload.order_id,
        gateway_order_id=str(uuid.uuid4()),
        status="CREATED"
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment
