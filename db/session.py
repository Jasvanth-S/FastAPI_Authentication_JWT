from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:jasvanth@localhost/authdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
