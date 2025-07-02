from sqlalchemy import Column, Integer, String, Text, Date
from app.database import Base

class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    category = Column(String, index=True)
    createdat = Column(Date)
    date = Column(Date)
    description = Column(Text)
    endsellingdate = Column(Date)
    holdtickets = Column(Integer)
    imageurl = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    organizer = Column(String)
    organizerdescription = Column(String)
    price = Column(Integer)
    slug = Column(String)
    startsellingdate = Column(Date)
    status = Column(String)
    stuckpending = Column(Integer)
    ticketsavailable = Column(Integer)
    ticketssold = Column(Integer)
    time = Column(Date)
    updatedat = Column(Date)
    userid = Column(String)
    venue = Column(String)
