from src.dao.profit_dao import ProfitDAO

dao = ProfitDAO()

def view_profit():
    cust_id = int(input("Enter customer ID: "))
    month = input("Enter month (YYYY-MM): ").strip()
    profit_amount = dao.calculate_profit(cust_id, month)
    print(f"✅ Profit for customer {cust_id} in {month}: {profit_amount}")

def list_profits():
    print("\n---- All Profits ----")
    profits = dao.get_all_profits()
    if not profits:
        print("No profit records found.")
        return
    for p in profits:
        print(f"Customer ID: {p.cust_id}, Period: {p.period}, Amount: {p.amount}, Created At: {p.created_at}")

def main():
    while True:
        print("\n=== Profits Management ===")
        print("1. View Profit for Customer")
        print("2. List All Profits")
        print("3. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            view_profit()
        elif choice == "2":
            list_profits()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
