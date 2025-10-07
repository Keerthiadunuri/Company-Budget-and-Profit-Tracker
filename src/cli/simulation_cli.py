from src.dao.simulation_dao import SimulationDAO
from src.models.simulation import Simulation

dao = SimulationDAO()

def add_simulation():
    print("---- Add New Simulation ----")
    cust_id = int(input("Enter customer ID: "))
    scenario = input("Enter scenario description: ").strip()
    projected_amount = float(input("Enter projected amount: "))

    simulation = Simulation(
        cust_id=cust_id,
        scenario=scenario,
        projected_amount=projected_amount
    )
    result = dao.create_simulation(simulation)
    print("✅ Simulation added:", result)

def list_simulations():
    print("---- All Simulations ----")
    simulations = dao.get_all_simulations()
    if not simulations:
        print("No simulations found.")
        return
    for s in simulations:
        print(f"ID: {s.simulation_id}, Customer: {s.cust_id}, Scenario: {s.scenario}, Amount: {s.projected_amount}")

def main():
    while True:
        print("\n=== Simulation Management ===")
        print("1. Add Simulation")
        print("2. List Simulations")
        print("3. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_simulation()
        elif choice == "2":
            list_simulations()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
