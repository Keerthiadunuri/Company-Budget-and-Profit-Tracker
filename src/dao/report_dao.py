from src.config.config import get_supabase_client
from src.models.report import Report

class ReportDAO:
    def __init__(self):
        self.supabase = get_supabase_client()

    def create_report(self, report: Report):
        data = {
            "cust_id": report.cust_id,
            "type": report.type,
            "content": report.content
        }
        response = self.supabase.table("reports").insert(data).execute()
        return response.data

    def get_all_reports(self):
        response = self.supabase.table("reports").select("*").execute()
        return [Report(**row) for row in response.data]

    def get_reports_by_customer(self, cust_id: int):
        response = self.supabase.table("reports").select("*").eq("cust_id", cust_id).execute()
        return [Report(**row) for row in response.data]
