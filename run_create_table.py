# run_create_table.py
from app.database import engine
from app.models.ticket import Base

Base.metadata.create_all(bind=engine)
