from sqlalchemy.orm import Session
from app.models.cart import CartItem
from app.models.product import Product

def calculate_cart_total(user_id: int, db: Session) -> float:
    items = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    total = 0.0

    for item in items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        total += product.price * item.quantity

    return total
