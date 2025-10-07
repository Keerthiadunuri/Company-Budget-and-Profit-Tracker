from src.models.customer import Customer
from src.dao.customer_dao import CustomerDAO

def add_customer():
    print("---- Add New Customer ----")
    
    # Get input from user
    name = input("Enter customer name: ").strip()
    email = input("Enter customer email: ").strip()
    phone = input("Enter customer phone: ").strip()
    city = input("Enter customer city: ").strip()

    # Create Customer object
    customer = Customer(name=name, email=email, phone=phone, city=city)

    # Insert into database
    dao = CustomerDAO()
    result = dao.create_customer(customer)

    print("\n✅ Customer added successfully!")
    print(result)

def list_customers():
    print("\n---- List of Customers ----")
    dao = CustomerDAO()
    customers = dao.get_all_customers()
    if not customers:
        print("No customers found.")
        return
    for c in customers:
        print(f"ID: {c.cust_id}, Name: {c.name}, Email: {c.email}, Phone: {c.phone}, City: {c.city}")

def main():
    while True:
        print("\n=== Customer Management ===")
        print("1. Add Customer")
        print("2. List Customers")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_customer()
        elif choice == "2":
            list_customers()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
