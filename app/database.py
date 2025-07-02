# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from dotenv import load_dotenv
# import os
# from pathlib import Path

# # Load .env from project root
# load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

# DATABASE_URL = os.getenv("DATABASE_URL")
# print("📦 DATABASE_URL:", DATABASE_URL)  # Debug output

# # Setup engine & session
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # DATABASE_URL=postgresql://postgres:nZIcdbapwVvIpjuKAJbhezrkzMxlNvIs@shortline.proxy.rlwy.net:39440/railway # untuk local
# #DATABASE_URL=postgresql://postgres:nZIcdbapwVvIpjuKAJbhezrkzMxlNvIs@postgres.railway.internal:5432/railway # ganti dari Railway PostgreSQL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from .env file
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")
print("📦 DATABASE_URL:", DATABASE_URL)  # Debug

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
