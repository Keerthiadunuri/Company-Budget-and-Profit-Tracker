import calendar
from src.config.config import get_supabase_client
from src.models.profit import Profit

class ProfitDAO:
    def __init__(self):
        self.supabase = get_supabase_client()

    def create_profit(self, profit: Profit):
        data = {
            "cust_id": profit.cust_id,
            "period": profit.period,
            "amount": profit.amount
        }
        response = self.supabase.table("profits").insert(data).execute()
        return response.data

    def get_all_profits(self):
        response = self.supabase.table("profits").select("*").execute()
        return [Profit(**row) for row in response.data]

    def get_profit_by_customer(self, cust_id: int):
        response = self.supabase.table("profits").select("*").eq("cust_id", cust_id).execute()
        return [Profit(**row) for row in response.data]

    # ✅ This must be indented inside the class
    def calculate_profit(self, cust_id: int, month: str):
        # month format: "YYYY-MM"
        year, month_num = map(int, month.split("-"))
        last_day = calendar.monthrange(year, month_num)[1]
        start_date = f"{year}-{month_num:02d}-01"
        end_date = f"{year}-{month_num:02d}-{last_day:02d}"

        # Fetch revenues
        rev_resp = self.supabase.table("transactions").select("amount")\
            .eq("cust_id", cust_id).eq("type", "revenue")\
            .gte("date", start_date).lte("date", end_date).execute()
        total_revenue = sum([r['amount'] for r in rev_resp.data]) if rev_resp.data else 0

        # Fetch expenses
        exp_resp = self.supabase.table("transactions").select("amount")\
            .eq("cust_id", cust_id).eq("type", "expense")\
            .gte("date", start_date).lte("date", end_date).execute()
        total_expense = sum([e['amount'] for e in exp_resp.data]) if exp_resp.data else 0

        profit_amount = total_revenue - total_expense

        # Create profit record
        profit = Profit(cust_id=cust_id, period=month, amount=profit_amount)
        self.create_profit(profit)
        return profit_amount
