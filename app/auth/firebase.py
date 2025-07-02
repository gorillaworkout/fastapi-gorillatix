import firebase_admin
from firebase_admin import credentials, auth
from pathlib import Path

cred_path = Path(__file__).parent.parent / "firebase" / "gorillatix-adminsdk.json"
print(f"Using Firebase Admin SDK JSON path: {cred_path}")

cred = credentials.Certificate(str(cred_path))
firebase_admin.initialize_app(cred)

def verify_firebase_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        print("Token received:", id_token)
        return decoded_token
    except Exception as e:
        print("Firebase token verification failed:", e)
        return None
