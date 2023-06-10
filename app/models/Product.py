from app.database import Base
from sqlalchemy import Column, Integer, JSON, Numeric, DateTime, String, Enum, func
from sqlalchemy.orm import relationship


class Product(Base):
    # Define table name
    __tablename__ = "products"
    # Define table columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    ingredients = Column(JSON, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    image = Column(String, nullable=True)
    type = Column(Enum("Main", "Extra"), nullable=True)
    date_created = Column(DateTime, default=func.now())
    date_modified = Column(DateTime, default=func.now(), onupdate=func.now())
    orders = relationship('ProductOrder', back_populates='product')


