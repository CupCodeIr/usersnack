from app.database import Base
from sqlalchemy import Column, Integer, DateTime, String, func
from sqlalchemy.orm import relationship

class Order(Base):
    # Define table name
    __tablename__ = "orders"
    # Define table columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    date_created = Column(DateTime, default=func.now())
    date_modified = Column(DateTime, default=func.now(), onupdate=func.now())
    items = relationship('ProductOrder', back_populates='order')