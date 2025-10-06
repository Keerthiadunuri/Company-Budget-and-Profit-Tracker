from dotenv import load_dotenv
import os
from supabase import create_client

# Load environment variables from .env
load_dotenv()

# Get Supabase URL and KEY from .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_supabase_client():
    """
    Returns a Supabase client for database operations
    """
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Supabase URL or KEY not set in .env")
    
    return create_client(SUPABASE_URL, SUPABASE_KEY)
