from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.ticket import Ticket

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")  # <-- ini harus /
def read_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()
