from pydantic import BaseModel
from typing import List

class OrderInput(BaseModel):
    products_id: List[int]
    customer_name: str
    address: str


class OrderOutput(BaseModel):
    order_id: int
    status: str = "success"
    message: str = ""
    total_price: float
    product_count: int


class CalculateOutput(BaseModel):
    status: str = "success"
    message: str = ""
    total_price: float
    total_products: int
