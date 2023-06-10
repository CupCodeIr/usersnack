from app.models.Order import Order
from app.models.Product import Product
from app.models.ProductOrder import ProductOrder
from sqlalchemy import inspect
import random


def seed_order(session):
    """
    Seed orders table with data
    :param session: SQLAlchemy session
    :return:
    """
    # Define sample order details
    sample_orders = [
        {
            'customer_name': 'Anna Müller',
            'address': 'Landstraße 1, 4020 Linz, Austria',
        },
        {
            'customer_name': 'Markus Schmidt',
            'address': 'Hauptplatz 2, 4020 Linz, Austria',
        },
        {
            'customer_name': 'Lisa Wagner',
            'address': 'Mozartstraße 3, 4020 Linz, Austria',
        },
    ]
    # Get all current products in database
    products = session.query(Product).all()
    for sample in sample_orders:
        # Get random product and extras
        product_id = random.randint(0, 13)
        extra1_id, extra2_id = random.randint(14, 19), random.randint(14, 19)
        # Create new order
        order = Order(customer_name=sample['customer_name'], address=sample['address'])
        # Create associations
        order_product = ProductOrder(price=products[product_id].price)
        order_extra1 = ProductOrder(price=products[extra1_id].price)
        order_extra2 = ProductOrder(price=products[extra2_id].price)
        # Associate order with products
        order_product.order = order_extra1.order = order_extra2.order = order
        order_product.product = products[product_id]
        order_extra1.product = products[extra1_id]
        order_extra2.product = products[extra2_id]

        session.add(order)
        session.add(order_product)
        session.add(order_extra1)
        session.add(order_extra2)

    session.commit()


def if_create_order_product_table(base, engine):
    """
    Creates association orders_products table if it doesn't exist
    :param base: SQLAlchemy base model
    :param engine: SQLAlchemy engine
    :return:
    """
    if not inspect(engine).has_table(ProductOrder.__tablename__):
        base.metadata.tables[ProductOrder.__tablename__].create(bind=engine)


def if_create_order_table(base, engine):
    """
    Creates orders table if it doesn't exist
    :param base: SQLAlchemy base model
    :param engine: SQLAlchemy engine
    :return:
    """
    if not inspect(engine).has_table(Order.__tablename__):
        base.metadata.tables[Order.__tablename__].create(bind=engine)
