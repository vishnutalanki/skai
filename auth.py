from supabase import create_client, Client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def sign_up(email: str, password: str):
    response = supabase.auth.sign_up({"email": email, "password": password})
    return response

def sign_in(email: str, password: str):
    response = supabase.auth.sign_in_with_password({"email": email, "password": password})
    return response
