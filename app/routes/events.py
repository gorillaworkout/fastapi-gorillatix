from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.events import Events
from app.database import get_db
from pydantic import BaseModel, Field
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
    holdTickets: int = 0
    imageUrl: str
    latitude: Optional[str]
    longitude: Optional[str]
    organizer: str
    organizerDescription: str
    price: int
    slug: str
    startSellingDate: str
    status: str
    stuckPending: int = 0
    ticketsAvailable: int
    ticketsSold: int
    time: str
    timeSelling: str
    title: str
    updatedAt: Optional[datetime] = None
    userId: str = Field(alias="userId")
    venue: str

    class Config:
        allow_population_by_field_name = True  # biar camelCase bisa diterima

@router.get("/")
def get_all_events(db: Session = Depends(get_db)):
    events = db.query(Events).all()

    if not events:
        raise HTTPException(status_code=404, detail="No events found")

    return [e.__dict__ for e in events]  # simpel

@router.post("/")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    print("📥 Incoming event payload:", event.dict(by_alias=True))  # Debug

    new_event = Events(**event.dict(by_alias=True))
    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    print(new_event,'new event')

    return {
        "message": "✅ Event successfully created",
        "event": {
            "id": new_event.id,
            "title": new_event.title,
            "date": new_event.date,
            "venue": new_event.venue,
            "status": new_event.status,
        }
    }
