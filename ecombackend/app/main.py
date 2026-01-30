from fastapi import FastAPI
from app.database import Base, engine
from app.auth.routes import router as auth_router
from app.products.routes import router as product_router
from app.orders.routes import router as order_router
from app.payments.routes import router as payment_router
from app.cart.routes import router as cart_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Commerce Backend")

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(payment_router)
app.include_router(cart_router)
