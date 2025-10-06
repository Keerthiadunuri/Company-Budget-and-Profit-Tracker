from src.dao.manager_dao import ManagerDAO
from src.models.manager import Manager

dao = ManagerDAO()

def add_manager():
    print("---- Add New Manager ----")
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone (optional): ").strip() or None

    manager = Manager(name=name, email=email, phone=phone)
    result = dao.create_manager(manager)
    print("✅ Manager added:", result)

def list_managers():
    print("---- All Managers ----")
    managers = dao.get_all_managers()
    if not managers:
        print("No managers found.")
        return
    for m in managers:
        print(f"ID: {m.manager_id}, Name: {m.name}, Email: {m.email}, Phone: {m.phone}")

def delete_manager():
    manager_id = int(input("Enter manager ID to delete: "))
    result = dao.delete_manager(manager_id)
    print("✅ Manager deleted:", result)

def main():
    while True:
        print("\n=== Manager Management ===")
        print("1. Add Manager")
        print("2. List Managers")
        print("3. Delete Manager")
        print("4. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_manager()
        elif choice == "2":
            list_managers()
        elif choice == "3":
            delete_manager()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
