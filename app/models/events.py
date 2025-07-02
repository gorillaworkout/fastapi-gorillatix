from sqlalchemy import Column, Integer, String, Text, Date
from app.database import Base

class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    category = Column(String, index=True)
    createdAt = Column(Date)
    date = Column(Date)
    description = Column(Text)
    endSellingDate = Column(Date)
    holdTickets = Column(Integer)
    imageUrl = Column(String)
    latitude = Column(String)
    location = Column(String)
    longitude = Column(String)
    organizer = Column(String)
    organizerDescription = Column(String)
    price = Column(Integer)
    slug = Column(String)
    startSellingDate = Column(Date)
    status = Column(String)
    stuckPending = Column(Integer)
    ticketsAvailable = Column(Integer)
    ticketsSold = Column(Integer)
    time = Column(Date)
    timeSelling = Column(Date)
    title = Column(String)
    updatedAt = Column(Date)
    userid = Column(String)
    venue = Column(String)
