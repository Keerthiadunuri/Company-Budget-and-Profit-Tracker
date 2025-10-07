import os
import streamlit as st
from supabase import create_client

def get_supabase_client():
    # Try Streamlit Secrets first
    SUPABASE_URL = st.secrets.get("SUPABASE_URL") if "SUPABASE_URL" in st.secrets else None
    SUPABASE_KEY = st.secrets.get("SUPABASE_KEY") if "SUPABASE_KEY" in st.secrets else None

    # Fallback to .env
    if not SUPABASE_URL or not SUPABASE_KEY:
        from dotenv import load_dotenv
        load_dotenv()
        SUPABASE_URL = SUPABASE_URL or os.getenv("SUPABASE_URL")
        SUPABASE_KEY = SUPABASE_KEY or os.getenv("SUPABASE_KEY")

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError(
            "❌ Missing Supabase credentials. Set them in .env (local) or Streamlit Secrets (deployed)."
        )

    return create_client(SUPABASE_URL, SUPABASE_KEY)
