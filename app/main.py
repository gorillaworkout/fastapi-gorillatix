import os
import sys
print(sys.path)
from fastapi import FastAPI
from sqlalchemy import text
from app.database import SessionLocal, Base, engine
from app.routes import events, tickets  # pastikan kamu juga punya tickets router

print("Active DATABASE_URL:", os.getenv("DATABASE_URL"))

app = FastAPI()

# Buat tabel jika belum ada
Base.metadata.create_all(bind=engine)

app.include_router(events.router, prefix="/events")
app.include_router(tickets.router, prefix="/tickets")

try:
    db = SessionLocal()
    db.execute(text("SELECT 1"))
    print(f"📦 DATABASE_URL: {os.getenv('DATABASE_URL')}")
    print("✅ Successfully connected to the database.")
except Exception as e:
    print(f"📦 DATABASE_URL: {os.getenv('DATABASE_URL')}")
    print("❌ Database connection failed:", e)
finally:
    db.close()
