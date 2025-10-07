from src.services.transaction_service import TransactionService

service = TransactionService()

def add_transaction():
    print("---- Add New Transaction ----")
    cust_id = int(input("Enter customer ID: "))
    type_ = input("Enter type (revenue/expense): ").strip().lower()
    amount = float(input("Enter amount: "))
    category = input("Enter category: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    description = input("Enter description (optional): ").strip()

    result = service.add_transaction(cust_id, type_, amount, category, date, description)
    print("✅ Transaction added:", result)

def list_customer_transactions():
    cust_id = int(input("Enter customer ID to view transactions: "))
    transactions = service.get_customer_transactions(cust_id)
    if not transactions:
        print("No transactions found.")
        return
    print(f"\nTransactions for Customer ID {cust_id}:")
    for t in transactions:
        print(f"ID: {t.trans_id}, Type: {t.type}, Amount: {t.amount}, Category: {t.category}, Date: {t.date}, Desc: {t.description}")

def main():
    while True:
        print("\n=== Transaction Management ===")
        print("1. Add Transaction")
        print("2. List Customer Transactions")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_transaction()
        elif choice == "2":
            list_customer_transactions()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
