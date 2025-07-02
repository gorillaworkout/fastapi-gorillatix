from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.auth.jwt import create_access_token
from pydantic import BaseModel
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginForm(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(form: LoginForm, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form.email).first()

    if not user or not pwd_context.verify(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"id": user.id})
    return {"access_token": token, "token_type": "bearer"}
