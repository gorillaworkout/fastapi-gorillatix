from sqlalchemy import Column, String, TIMESTAMP, text
from app.database import Base  # ✅ ini yang digunakan sebagai parent class

class Users(Base):
    __tablename__ = "users"

    uid = Column(String, primary_key=True, index=True)
    email = Column(String, nullable=False)
    display_name = Column(String)
    photo_url = Column(String)
    role = Column(String, default="user")
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
