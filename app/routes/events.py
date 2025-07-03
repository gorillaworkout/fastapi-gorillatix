from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.events import Events
from app.database import get_db
from app.auth.dependencies import admin_required
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.models.user import User

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
        validate_by_name = True

@router.get("/")
def get_all_events(db: Session = Depends(get_db)):
    events = db.query(Events).all()
    return [e.__dict__ for e in events]  # Tetap return [] jika kosong


@router.post("/create")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Events(**event.dict(by_alias=True))
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
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

@router.delete("/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required),  # hanya admin boleh akses
):
    event = db.query(Events).filter(Events.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(event)
    db.commit()

    return {"message": f"Event with ID {event_id} deleted successfully"}
