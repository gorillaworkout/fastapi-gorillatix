import os
import sys
print(sys.path)

from fastapi import FastAPI
from sqlalchemy import text
from app.database import SessionLocal, Base, engine
from app.routes import events, tickets
from fastapi.middleware.cors import CORSMiddleware

print("Active DATABASE_URL:", os.getenv("DATABASE_URL"))

app = FastAPI()


# origins = [
#     "http://localhost:3000",  # untuk local dev
#     "https://gorillatix.com",  # untuk production
# ]

app.add_middleware(
    CORSMiddleware=["*"],
    allow_origins=origins,          # jangan pakai ["*"] kalau allow_credentials=True
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Buat tabel jika belum ada
Base.metadata.create_all(bind=engine)

# Tes koneksi DB saat startup
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

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to GorillaTix API"}

# Routers
app.include_router(events.router, prefix="/events")
app.include_router(tickets.router, prefix="/tickets")
