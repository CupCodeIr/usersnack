import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from app.seeders.product_seeder import if_create_product_table, seed_product
from app.seeders.order_seeder import if_create_order_table, if_create_order_product_table, seed_order
from app.database import SessionLocal, Base, engine

# First seed the products table
if_create_product_table(Base, engine)
seed_product(SessionLocal())

# Then seed the orders table with associated products
if_create_order_product_table(Base, engine)
if_create_order_table(Base, engine)
seed_order(SessionLocal())
