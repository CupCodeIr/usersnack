from fastapi import FastAPI, Request, Query, HTTPException
from fastapi.middleware import Middleware
from fastapi.staticfiles import StaticFiles
from app.middlewares.DBSessionMiddleware import DBSessionMiddleware
from app.models.Product import Product
from sqlalchemy.orm import defer
from sqlalchemy import func
from app.schema.Order import OrderInput, OrderOutput, CalculateOutput
from app.models.Order import Order
from app.models.ProductOrder import ProductOrder
import os
from typing import Annotated

root_path = os.path.dirname(os.path.abspath(__file__))
app = FastAPI(title='Usersnack',
              description='A fast and simple API for Usersnack application<br><br>Accessing to image files through base path: <code>/storage/images</code>',
              middleware=[Middleware(DBSessionMiddleware)])

exclude_date_modified = defer(Product.date_modified)
exclude_date_created = defer(Product.date_created)
app.mount("/storage", StaticFiles(directory=os.path.join(root_path, "storage")), name="storage")


@app.get("/")
async def root():
    return {"message": "Hello World! Check the docs at /docs"}


@app.get("/products/")
async def get_products(request: Request) -> dict[str, list]:
    """
    Retrun products details
    :param request: request
    :return:
    """
    db_session = request.state.db
    products = []
    # exclude unnecessary columns
    products = db_session.query(Product).options(exclude_date_created, exclude_date_modified).all()

    return {"products": products}


@app.get("/products/{product_id}")
async def get_product(request: Request, product_id: int = None) -> dict[str, list]:
    """
    Retrun product details
    :param product_id: product id to retrieve
    :param request: request
    :return:
    """
    db_session = request.state.db
    products = [db_session.query(Product).options(exclude_date_created, exclude_date_modified).get(product_id)]
    # exclude unnecessary columns
    if not isinstance(products[0], Product):
        raise HTTPException(status_code=404, detail="Product Not Found!")
    return {"products": products}


@app.get('/order/calculate/')
async def get_order_total(request: Request, products_id: Annotated[list[int], Query()]) -> CalculateOutput:
    """
    Return order total price
    :param request: request
    :param products_id: comma seperated products id
    :return: json
    object containing status, message, total_price and product_count. Ensure product_count is equal to the number of
    requested products otherwise there maybe some non-existing product ids in your request
    """
    session = request.state.db
    total_price = session.query(func.sum(Product.price)).filter(Product.id.in_(products_id)).scalar() or 0
    total_products = session.query(Product.price).filter(Product.id.in_(products_id)).count()
    message = ""
    status = "success"
    if not (len(products_id) == total_products):
        message = "One or more products does not exist!"
        status = "failure"

    return CalculateOutput(status=status, message=message, total_price=total_price, total_products=total_products)


@app.post('/order/')
async def store_order(request: Request, input_order: OrderInput) -> OrderOutput:
    """
    Store order data
    :param input_order: order to be submitted
    :param request: request
    :return: json
    object containing status, message, total_price and product_count. Ensure product_count is equal to the number of
    requested products otherwise there maybe some non-existing product ids in your request
    """
    session = request.state.db
    products_id = input_order.products_id
    customer_name = input_order.customer_name
    address = input_order.address
    products = session.query(Product).filter(Product.id.in_(products_id)).all() or []
    message = ""
    status = "success"
    found_product_len = len(products)
    total_price = 0
    order = None
    if len(products_id) == found_product_len:
        order = Order(customer_name=customer_name, address=address)
        session.add(order)
        for product in products:
            order_product = ProductOrder(price=product.price)
            # Associate order with products
            order_product.order = order
            order_product.product = product

            session.add(order_product)
            total_price += product.price

        session.commit()
    else:
        message = "Order did not submitted, one or more products does not exist!"
        status = "failure"
    order_id = order.id if order else 0
    return OrderOutput(order_id=order_id, status=status, message=message, total_price=total_price,
                       product_count=found_product_len)
