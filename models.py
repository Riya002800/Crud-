from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from database import Base

# Define the User table as a Python class
class User(Base):
    __tablename__ = 'users'  # This will be the table name in MySQL

    id = Column(Integer, primary_key=True, index=True)  # Unique ID
    name = Column(String(50))  # User name
    email = Column(String(100), unique=True, index=True)  # User email (must be unique)
