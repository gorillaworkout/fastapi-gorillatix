from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String, unique=True, index=True) 
    email = Column(String, unique=True, index=True)
    role = Column(String, default="user")  # "admin" or "user"
