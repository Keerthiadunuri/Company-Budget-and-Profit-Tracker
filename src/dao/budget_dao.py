from src.config.config import get_supabase_client
from src.models.budget import Budget

class BudgetDAO:
    def __init__(self):
        self.supabase = get_supabase_client()

    def create_budget(self, budget: Budget):
        data = {
            "category": budget.category,
            "planned_amount": budget.planned_amount,
            "actual_amount": budget.actual_amount,
            "start_date": budget.start_date,
            "end_date": budget.end_date
        }
        response = self.supabase.table("budgets").insert(data).execute()
        return response.data

    def get_all_budgets(self):
        response = self.supabase.table("budgets").select("*").execute()
        return [Budget(**row) for row in response.data]

    def update_actual_amount(self, budget_id: int, actual_amount: float):
        response = self.supabase.table("budgets").update({"actual_amount": actual_amount}).eq("budget_id", budget_id).execute()
        return response.data
