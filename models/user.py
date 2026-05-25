"""
Model: User
Tabel: users
Kolom: id, name, email, password_hash, role (customer/owner), phone, created_at
"""
from api.supabase_client import get_client

TABLE = "users"

def get_all():
    return get_client().table(TABLE).select("*").execute().data

def get_by_email(email: str):
    return get_client().table(TABLE).select("*").eq("email", email).single().execute().data

def create(name: str, email: str, password_hash: str, role: str, phone: str = ""):
    return get_client().table(TABLE).insert({
        "name": name, "email": email, "password_hash": password_hash,
        "role": role, "phone": phone
    }).execute().data

def update(user_id: str, data: dict):
    return get_client().table(TABLE).update(data).eq("id", user_id).execute().data

def delete(user_id: str):
    return get_client().table(TABLE).delete().eq("id", user_id).execute().data
