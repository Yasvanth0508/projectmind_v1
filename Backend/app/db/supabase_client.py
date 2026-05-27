from app.config import settings
from supabase import create_client, Client

SUPABASE_URL = settings.supabase_url
SUPABASE_KEY = settings.supabase_key

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
