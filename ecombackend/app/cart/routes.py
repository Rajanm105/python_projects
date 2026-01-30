from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.dependencies import get_current_user
from app.models.cart import CartItem
from app.models.product import Product
from app.schemas.cart import CartAdd, CartUpdate, CartItemResponse
from app.models.user import User

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.post("/add", response_model=CartItemResponse)
def add_to_cart(
    payload: CartAdd,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == payload.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    cart_item = db.query(CartItem).filter(
        CartItem.user_id == current_user.id,
        CartItem.product_id == payload.product_id
    ).first()

    if cart_item:
        cart_item.quantity += payload.quantity
    else:
        cart_item = CartItem(
            user_id=current_user.id,
            product_id=payload.product_id,
            quantity=payload.quantity
        )
        db.add(cart_item)

    db.commit()
    db.refresh(cart_item)
    return cart_item


@router.get("/", response_model=list[CartItemResponse])
def view_cart(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(CartItem).filter(
        CartItem.user_id == current_user.id
    ).all()


@router.put("/{cart_item_id}", response_model=CartItemResponse)
def update_cart_item(
    cart_item_id: int,
    payload: CartUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    cart_item = db.query(CartItem).filter(
        CartItem.id == cart_item_id,
        CartItem.user_id == current_user.id
    ).first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    cart_item.quantity = payload.quantity
    db.commit()
    db.refresh(cart_item)
    return cart_item

@router.delete("/{cart_item_id}")
def remove_cart_item(
    cart_item_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    cart_item = db.query(CartItem).filter(
        CartItem.id == cart_item_id,
        CartItem.user_id == current_user.id
    ).first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    db.delete(cart_item)
    db.commit()
    return {"message": "Item removed from cart"}

