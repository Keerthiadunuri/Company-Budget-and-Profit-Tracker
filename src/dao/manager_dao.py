from src.config.config import get_supabase_client
from src.models.manager import Manager

class ManagerDAO:
    def __init__(self):
        self.supabase = get_supabase_client()

    def create_manager(self, manager: Manager):
        data = {
            "name": manager.name,
            "email": manager.email,
            "phone": manager.phone
        }
        response = self.supabase.table("managers").insert(data).execute()
        return response.data

    def get_all_managers(self):
        response = self.supabase.table("managers").select("*").execute()
        return [Manager(**row) for row in response.data]

    def get_manager_by_id(self, manager_id: int):
        response = self.supabase.table("managers").select("*").eq("manager_id", manager_id).execute()
        if response.data:
            return Manager(**response.data[0])
        return None

    def delete_manager(self, manager_id: int):
        response = self.supabase.table("managers").delete().eq("manager_id", manager_id).execute()
        return response.data
