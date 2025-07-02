from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.events import Events
from app.database import get_db
from pydantic import BaseModel  # ✅ tambahkan ini
from datetime import datetime
from typing import Optional


router = APIRouter()

class EventCreate(BaseModel):
    address: str
    category: str
    createdAt: Optional[datetime] = None
    date: str
    description: str
    endSellingDate: str
    holdTickets: int
    imageUrl: str
    latitude: Optional[str]
    longitude: Optional[str]
    organizer: str
    organizerDescription: str
    price: int
    slug: str
    startSellingDate: str
    status: str
    stuckPending: int
    ticketsAvailable: int
    ticketsSold: int
    time: str
    timeSelling: str
    title: str
    updatedAt: Optional[datetime] = None
    userid: str
    venue: str

@router.get("/")
def get_all_events(db: Session = Depends(get_db)):
    events = db.query(Events).all()

    if not events:
        raise HTTPException(status_code=404, detail="No events found")

    return [
        {
            "id": e.id,
            "address": e.address,
            "category": e.category,
            "createdAt": e.createdAt,
            "date": e.date,
            "description": e.description,
            "endSellingDate": e.endSellingDate,
            "holdTickets": e.holdTickets,
            "imageUrl": e.imageUrl,
            "latitude": e.latitude,
            "longitude": e.longitude,
            "organizer": e.organizer,
            "organizerDescription": e.organizerDescription,
            "price": e.price,
            "slug": e.slug,
            "startSellingDate": e.startSellingDate,
            "status": e.status,
            "stuckPending": e.stuckPending,
            "ticketsAvailable": e.ticketsAvailable,
            "ticketsSold": e.ticketsSold,
            "time": e.time,
            "timeSelling": e.timeSelling,
            "title": e.title,
            "updatedAt": e.updatedAt,
            "userid": e.userid,
            "venue": e.venue
        }
        for e in events
    ]




@router.post("/")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Events(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event