from src.dao.report_dao import ReportDAO
from src.models.report import Report

dao = ReportDAO()

def add_report():
    cust_id = int(input("Enter customer ID: "))
    type_ = input("Enter report type (e.g., monthly, yearly): ").strip()
    content = input("Enter report content: ").strip()

    report = Report(cust_id=cust_id, type=type_, content=content)
    result = dao.create_report(report)
    print("✅ Report added:", result)

def list_reports():
    print("\n---- All Reports ----")
    reports = dao.get_all_reports()
    if not reports:
        print("No reports found.")
        return
    for r in reports:
        print(f"ID: {r.report_id}, Customer ID: {r.cust_id}, Type: {r.type}, Content: {r.content}, Created At: {r.created_at}")

def main():
    while True:
        print("\n=== Reports Management ===")
        print("1. Add Report")
        print("2. List Reports")
        print("3. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_report()
        elif choice == "2":
            list_reports()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
