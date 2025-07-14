from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import Base

engine = create_engine("sqlite:///restaurant.db")
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)