from src.config.config import get_supabase_client
from src.models.customer import Customer

class CustomerDAO:
    def __init__(self):
        self.supabase = get_supabase_client()

    def create_customer(self, customer: Customer):
        data = {
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone,
            "city": customer.city
        }  
        response = self.supabase.table("customers").insert(data).execute()
        return response.data

    def get_all_customers(self):
        response = self.supabase.table("customers").select("*").execute()
        return [Customer(**row) for row in response.data]

    def get_customer_by_id(self, cust_id: int):
        response = self.supabase.table("customers").select("*").eq("cust_id", cust_id).execute()
        if response.data:
            return Customer(**response.data[0])
        return None

    def delete_customer(self, cust_id: int):
        response = self.supabase.table("customers").delete().eq("cust_id", cust_id).execute()
        return response.data
