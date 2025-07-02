from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.events import Events
from app.database import get_db

router = APIRouter()

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
