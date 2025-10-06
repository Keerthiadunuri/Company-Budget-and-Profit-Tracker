from src.config import get_supabase_client

supabase = get_supabase_client()

# Example: Fetch all customers
response = supabase.table("customers").select("*").execute()
print(response.data)
