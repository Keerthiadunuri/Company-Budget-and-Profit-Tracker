from src.config.config import get_supabase_client
from src.models.simulation import Simulation

class SimulationDAO:
    def __init__(self):
        self.supabase = get_supabase_client()

    def create_simulation(self, simulation: Simulation):
        data = {
            "cust_id": simulation.cust_id,
            "scenario": simulation.scenario,
            "projected_amount": simulation.projected_amount
        }
        response = self.supabase.table("simulations").insert(data).execute()
        return response.data

    def get_all_simulations(self):
        response = self.supabase.table("simulations").select("*").execute()
        return [Simulation(**row) for row in response.data]

    def get_simulations_by_customer(self, cust_id: int):
        response = self.supabase.table("simulations").select("*").eq("cust_id", cust_id).execute()
        return [Simulation(**row) for row in response.data]
