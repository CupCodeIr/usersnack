from app.database import Base
from sqlalchemy import Column, Integer, Numeric, DateTime, func, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship


class ProductOrder(Base):
    # Define table name
    __tablename__ = "products_orders"
    # Define table columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    price = Column(Numeric(10, 2), nullable=False)
    date_created = Column(DateTime, default=func.now())
    date_modified = Column(DateTime, default=func.now(), onupdate=func.now())
    #   Make sure we don't have any duplicate relation
    PrimaryKeyConstraint('order_id', 'product_id', name='pr_assoc')
    product = relationship('Product', back_populates='orders')
    order = relationship('Order', back_populates='items')