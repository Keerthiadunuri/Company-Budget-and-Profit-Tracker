from src.models.budget import Budget
from src.dao.budget_dao import BudgetDAO

dao = BudgetDAO()

def add_budget():
    print("---- Add New Budget ----")
    cust_id = int(input("Enter customer ID: ").strip())  # must exist in customers table
    category = input("Enter category: ").strip()
    planned_amount = float(input("Enter planned amount: ").strip())
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()

    budget = Budget(
        cust_id=cust_id,
        category=category,
        planned_amount=planned_amount,
        actual_amount=0,   # default actual amount
        start_date=start_date,
        end_date=end_date
    )

    result = dao.create_budget(budget)
    print("✅ Budget added:", result)


def list_budgets():
    print("\n---- All Budgets ----")
    budgets = dao.get_all_budgets()
    if not budgets:
        print("No budgets found.")
        return
    for b in budgets:
        print(f"ID: {b.budget_id}, Customer ID: {b.cust_id}, Category: {b.category}, Planned: {b.planned_amount}, Actual: {b.actual_amount}, Start: {b.start_date}, End: {b.end_date}")


def update_actual_budget():
    budget_id = int(input("Enter budget ID to update actual amount: ").strip())
    actual_amount = float(input("Enter actual amount: ").strip())
    result = dao.update_actual_amount(budget_id, actual_amount)
    print("✅ Budget updated:", result)


def main():
    while True:
        print("\n=== Budget Management ===")
        print("1. Add Budget")
        print("2. List Budgets")
        print("3. Update Actual Amount")
        print("4. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_budget()
        elif choice == "2":
            list_budgets()
        elif choice == "3":
            update_actual_budget()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
