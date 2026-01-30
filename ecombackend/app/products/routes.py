from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse
from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post("/", response_model=ProductResponse)
def create_product(payload: ProductCreate,current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    product = Product(**payload.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
