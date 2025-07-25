from fastapi import FastAPI
from sqlalchemy import text
from app.database import SessionLocal, Base, engine
from app.routes import events, tickets, auth, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://gorillatix-v2.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

try:
    db = SessionLocal()
    db.execute(text("SELECT 1"))
    print("✅ Database connected.")
except Exception as e:
    print("❌ Database error:", e)
finally:
    db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to GorillaTix API"}

app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(tickets.router, prefix="/tickets", tags=["Tickets"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api", tags=["Users"])


import json

# with open("app/firebase/gorillatix-adminsdk.json") as f:
#     data = json.load(f)

# env_ready = json.dumps(data)
# print(env_ready)