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
            "createdat": e.createdat,
            "date": e.date,
            "description": e.description,
            "endsellingdate": e.endsellingdate,
            "holdtickets": e.holdtickets,
            "imageurl": e.imageurl,
            "latitude": e.latitude,
            "longitude": e.longitude,
            "organizer": e.organizer,
            "organizerdescription": e.organizerdescription,
            "price": e.price,
            "slug": e.slug,
            "startsellingdate": e.startsellingdate,
            "status": e.status,
            "stuckpending": e.stuckpending,
            "ticketsavailable": e.ticketsavailable,
            "ticketssold": e.ticketssold,
            "time": e.time,
            "updatedat": e.updatedat,
            "userid": e.userid,
            "venue": e.venue
        }
        for e in events
    ]
