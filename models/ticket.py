from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    event_id = Column(String)
    quantity = Column(Integer)
