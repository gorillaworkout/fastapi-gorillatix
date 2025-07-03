from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from app.models.users import Users
from app.database import get_db

router = APIRouter()


# ===== Pydantic Schemas =====

class UserCreateRequest(BaseModel):
    uid: str
    email: EmailStr
    displayName: str | None = None
    photoURL: str | None = None

class RoleUpdateRequest(BaseModel):
    uid: str
    role: str  # "user" or "admin"


# ===== GET all users =====
@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()

    return {
        "message": f"{len(users)} users found",
        "users": [
            {
                "uid": user.uid,
                "email": user.email,
                "display_name": user.display_name,
                "photo_url": user.photo_url,
                "role": user.role,
                "created_at": user.created_at,
            }
            for user in users
        ]
    }


# ===== CREATE user =====
@router.post("/users/")
def create_user(user: UserCreateRequest, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.uid == user.uid).first()
    if db_user:
        return {"message": "User already exists."}

    new_user = Users(
        uid=user.uid,
        email=user.email,
        display_name=user.displayName,
        photo_url=user.photoURL,
        role="user"  # default role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created",
        "user": {
            "uid": new_user.uid,
            "email": new_user.email,
            "display_name": new_user.display_name,
            "photo_url": new_user.photo_url,
            "role": new_user.role,
            "created_at": new_user.created_at,
        }
    }


# ===== UPDATE user role =====
@router.patch("/users/role")
def update_user_role(data: RoleUpdateRequest, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.uid == data.uid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.role not in ("user", "admin"):
        raise HTTPException(status_code=400, detail="Invalid role. Must be 'user' or 'admin'.")

    user.role = data.role
    db.commit()
    db.refresh(user)

    return {
        "message": "User role updated successfully",
        "user": {
            "uid": user.uid,
            "email": user.email,
            "role": user.role
        }
    }
