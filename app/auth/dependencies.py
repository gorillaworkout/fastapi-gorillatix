from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users import Users
from app.auth.firebase import verify_firebase_token

def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    token = authorization.split(" ")[1]
    decoded_token = verify_firebase_token(token)
    if not decoded_token:
        raise HTTPException(status_code=401, detail="Invalid Firebase token")

    uid = decoded_token.get("uid")
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token: no UID")

    user = db.query(Users).filter(Users.uid == uid).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user

def admin_required(current_user: Users = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user
