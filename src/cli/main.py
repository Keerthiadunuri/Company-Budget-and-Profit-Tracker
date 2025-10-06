import streamlit as st
import sys
import os

# -------------------- PATH SETUP --------------------
# Make the project root accessible to Python
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

# -------------------- IMPORT CLI MODULES --------------------
from src.cli.customer_cli import add_customer, list_customers
from src.cli.transaction_cli import add_transaction, list_customer_transactions
from src.cli.budget_cli import add_budget, list_budgets, update_actual_budget
from src.cli.profit_cli import view_profit, list_profits
from src.cli.report_cli import add_report, list_reports
from src.cli.simulation_cli import add_simulation, list_simulations
from src.cli.manager_cli import add_manager, list_managers

# -------------------- SIDEBAR MENU --------------------
st.sidebar.title("Company Budget & Profit Tracker")
menu = st.sidebar.selectbox(
    "Select Module",
    ["Customers", "Transactions", "Budgets", "Profits", "Reports", "Simulations", "Managers"]
)

# -------------------- CUSTOMERS --------------------
if menu == "Customers":
    st.header("Customer Module")

    with st.expander("Add New Customer"):
        st.write("Use the form below to add a customer")
        # Use Streamlit input fields
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        city = st.text_input("City")
        if st.button("Submit Customer"):
            # Call CLI function with proper handling
            add_customer(name=name, email=email, phone=phone, city=city)
            st.success("Customer added successfully!")

    st.subheader("All Customers")
    list_customers()

# -------------------- TRANSACTIONS --------------------
elif menu == "Transactions":
    st.header("Transaction Module")

    with st.expander("Add Transaction"):
        cust_id = st.number_input("Customer ID", min_value=1)
        t_type = st.selectbox("Transaction Type", ["revenue", "expense"])
        amount = st.number_input("Amount", min_value=0.0, step=0.01)
        category = st.text_input("Category")
        description = st.text_input("Description")
        if st.button("Submit Transaction"):
            add_transaction(cust_id=cust_id, t_type=t_type, amount=amount,
                            category=category, description=description)
            st.success("Transaction added successfully!")

    st.subheader("Transactions by Customer")
    list_customer_transactions()

# -------------------- BUDGETS --------------------
elif menu == "Budgets":
    st.header("Budget Module")

    with st.expander("Add Budget"):
        cust_id = st.number_input("Customer ID", min_value=1, key="budget_cust")
        category = st.text_input("Category", key="budget_cat")
        planned_amount = st.number_input("Planned Amount", min_value=0.0, step=0.01)
        if st.button("Submit Budget"):
            add_budget(cust_id=cust_id, category=category, planned_amount=planned_amount)
            st.success("Budget added successfully!")

    with st.expander("Update Actual Amount"):
        update_actual_budget()

    st.subheader("All Budgets")
    list_budgets()

# -------------------- PROFITS --------------------
elif menu == "Profits":
    st.header("Profit Module")

    with st.expander("Calculate/View Profit"):
        view_profit()

    st.subheader("All Profits")
    list_profits()

# -------------------- REPORTS --------------------
elif menu == "Reports":
    st.header("Report Module")

    with st.expander("Add Report"):
        add_report()

    st.subheader("All Reports")
    list_reports()

# -------------------- SIMULATIONS --------------------
elif menu == "Simulations":
    st.header("Simulation Module")

    with st.expander("Add Simulation"):
        add_simulation()

    st.subheader("All Simulations")
    list_simulations()

# -------------------- MANAGERS --------------------
elif menu == "Managers":
    st.header("Manager Module")

    with st.expander("Add Manager"):
        add_manager()

    st.subheader("All Managers")
    list_managers()
