from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.users import Users
from app.database import get_db

router = APIRouter()

@router.post("/users/")
def create_user(user: dict, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.uid == user["uid"]).first()
    if db_user:
        return {"message": "User already exists."}

    new_user = Users(
        uid=user["uid"],
        email=user["email"],
        display_name=user.get("displayName"),
        photo_url=user.get("photoURL"),
        role="user"  # default role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created", "user": {
        "uid": new_user.uid,
        "email": new_user.email,
        "display_name": new_user.display_name,
        "photo_url": new_user.photo_url,
        "role": new_user.role,
        "created_at": new_user.created_at,
    }}
