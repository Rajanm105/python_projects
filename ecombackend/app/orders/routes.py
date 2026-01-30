from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderResponse
from app.auth.dependencies import get_current_user
from app.models.user import User
from app.cart.utils import calculate_cart_total
from app.models.cart import CartItem


router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderResponse)
def create_order(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    total = calculate_cart_total(current_user.id, db)

    if total <= 0:
        raise HTTPException(status_code=400, detail="Cart is empty")

    order = Order(
        user_id=current_user.id,
        total_amount=total,
        status="PENDING"
    )
    db.add(order)

    # Clear cart after order creation
    db.query(CartItem).filter(
        CartItem.user_id == current_user.id
    ).delete()

    db.commit()
    db.refresh(order)
    return order
