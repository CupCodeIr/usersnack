from app.models.Product import Product
from sqlalchemy import inspect


def seed_product(session):
    """
    Seed products table with data
    :param session: SQLAlchemy session
    :return:
    """
    products = [
        Product(name="Cheese & Tomato", ingredients=['tomato', 'cheese'], image="cheesetomato.jpg",
                type="Main", price=11.90),
        Product(name="Mighty Meaty",
                ingredients=['tomato', 'pepperoni', 'ham', 'onion', 'mushrooms', 'sausage'],
                image="mighty-meaty-pizza.jpg", type="Main", price=16.90),
        Product(name="Pepperoni Passion", ingredients=['tomato', 'pepperoni', 'cheese'],
                image="pepperoni-passion-pizza.jpg", type="Main", price=16.90),
        Product(name="Texas BBQ",
                ingredients=['bbq sauce', 'bacon', 'onion', 'roast chicken', 'green peppers'],
                image="texas-bbq-pizza.jpg", type="Main", price=16.90),
        Product(name="Vegi Supreme", ingredients=['tomato', 'onion', 'green peppers', 'mushrooms'],
                image="vegisupreme-pizza.jpg", type="Main", price=16.90),
        Product(name="American Hot", ingredients=['tomato', 'onion', 'pepperoni', 'jalapeno'],
                image="ahot_thumbnail.jpg", type="Main", price=15.90),
        Product(name="Chicken and Rasher Bacon",
                ingredients=['tomato', 'chicken breast', 'bacon', 'onion'],
                image="CHICKEN_RASHER_BACON.jpg", type="Main", price=15.90),
        Product(name="Chicken Feast", ingredients=['tomato', 'chicken', 'mushrooms'],
                image="chickenfeast.jpg", type="Main", price=15.90),
        Product(name="Four Vegi", ingredients=['tomato', 'spinach', 'onion', 'mushrooms'],
                image="FourVegi.jpg", type="Main", price=15.90),
        Product(name="Hot & Spicy",
                ingredients=['tomato', 'onion', 'beef', 'green peppers', 'jalapeno'],
                image="hot-n-spicy-pizza.jpg", type="Main", price=15.90),
        Product(name="Meateor",
                ingredients=['bbq sauce', 'cheese', 'pork meatballs', 'sausage', 'pepperoni', 'bacon'],
                image="meateor.jpg", type="Main", price=16.90),
        Product(name="New Yorker", ingredients=['tomato', 'pepperoni', 'bacon', 'mushrooms'],
                image="new-yorker.jpg", type="Main", price=16.90),
        Product(name="Tandoori Hot",
                ingredients=['tomato', 'chicken', 'onion', 'green peppers', 'jalapeno'],
                image="tandoori-hot-pizza.jpg", type="Main", price=16.90),
        Product(name="The Sizzler",
                ingredients=['tomato', 'garlic sauce', 'onion', 'pepperoni', 'jalapeno', 'green peppers'],
                image="TheSizzler80x56.jpg", type="Main", price=16.90),
        Product(name="ham", type="Extra", price=2),
        Product(name="onion", type="Extra", price=1),
        Product(name="bacon", type="Extra", price=2),
        Product(name="cheese", type="Extra", price=1.4),
        Product(name="green peppers", type="Extra", price=1.2),
        Product(name="mushrooms", type="Extra", price=1.2),
    ]

    session.bulk_save_objects(products)
    session.commit()


def if_create_product_table(base, engine):
    """
    Creates products table if it doesn't exist
    :param base: SQLAlchemy base model
    :param engine: SQLAlchemy engine
    :return:
    """
    if not inspect(engine).has_table(Product.__tablename__):
        base.metadata.tables[Product.__tablename__].create(bind=engine)
