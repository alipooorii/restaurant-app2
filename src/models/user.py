from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    employee_id = Column(String, unique=True, nullable=False)
    national_id = Column(String, nullable=False)
    password = Column(String, nullable=True)