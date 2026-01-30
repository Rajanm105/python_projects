from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    status = Column(String)
    gateway_order_id = Column(String)
