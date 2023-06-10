from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


root_path = os.path.dirname(os.path.abspath(__file__))
SQL_DB_URL = os.path.join(f"sqlite:///{root_path}", "usersnack_app.db")

engine = create_engine(SQL_DB_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
