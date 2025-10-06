from src.config.config import get_supabase_client
from src.models.transaction import Transaction

class TransactionDAO:
    def __init__(self):
        self.supabase = get_supabase_client()

    def create_transaction(self, transaction: Transaction):
        data = {
            "cust_id": transaction.cust_id,
            "type": transaction.type,
            "amount": transaction.amount,
            "category": transaction.category,
            "date": transaction.date,
            "description": transaction.description
        }
        response = self.supabase.table("transactions").insert(data).execute()
        return response.data

    def get_transactions_by_customer(self, cust_id: int):
        response = self.supabase.table("transactions").select("*").eq("cust_id", cust_id).execute()
        return [Transaction(**row) for row in response.data]

    def get_all_transactions(self):
        response = self.supabase.table("transactions").select("*").execute()
        return [Transaction(**row) for row in response.data]
