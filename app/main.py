from fastapi import FastAPI
from app.routes import ticket

app = FastAPI()
app.include_router(ticket.router)
