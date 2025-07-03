import os
import json
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, auth

load_dotenv()

firebase_cred_json = os.getenv("FIREBASE_CREDENTIALS")

if not firebase_cred_json:
    raise ValueError("FIREBASE_CREDENTIALS not found in environment")

# Tidak perlu replace apa-apa kalau pakai json.dumps saat generate
try:
    cred_dict = json.loads(firebase_cred_json)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)
except Exception as e:
    print("❌ Error initializing Firebase Admin SDK:", e)
    raise e

def verify_firebase_token(id_token: str):
    try:
        return auth.verify_id_token(id_token)
    except Exception as e:
        print("❌ Firebase token verification failed:", e)
        return None
