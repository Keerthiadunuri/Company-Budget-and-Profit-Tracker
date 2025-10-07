import streamlit as st
import sys
import os
from datetime import datetime

# -------------------- PATH SETUP --------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

# -------------------- IMPORT DAOS --------------------
from src.dao.customer_dao import CustomerDAO
from src.dao.transaction_dao import TransactionDAO
from src.dao.budget_dao import BudgetDAO
from src.dao.profit_dao import ProfitDAO
from src.dao.simulation_dao import SimulationDAO

# -------------------- INITIALIZE DAOS --------------------
customerDAO = CustomerDAO()
transactionDAO = TransactionDAO()
budgetDAO = BudgetDAO()
profitDAO = ProfitDAO()
simulationDAO = SimulationDAO()

# -------------------- SIDEBAR MENU --------------------
st.sidebar.title("Company Budget & Profit Tracker")
menu = st.sidebar.selectbox(
    "Select Module",
    ["Customers", "Transactions", "Budgets", "Profits", "Simulations"]
)

# -------------------- CUSTOMERS --------------------
from src.models.customer import Customer
from src.models.transaction import Transaction

if menu == "Customers":
    st.header("Customer Module")
    
    with st.expander("Add Customer"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        city = st.text_input("City")
        if st.button("Submit Customer"):
            customer_obj = Customer(name=name, email=email, phone=phone, city=city)
            result = customerDAO.create_customer(customer_obj)
            st.success(f"Customer added successfully: {result}")
    
    st.subheader("All Customers")
    customers = customerDAO.get_all_customers()
    if customers:
        st.table([vars(c) for c in customers])
    else:
        st.info("No customers yet.")

# -------------------- TRANSACTIONS --------------------
elif menu == "Transactions":
    st.header("Transaction Module")

    with st.expander("Add Transaction"):
        cust_id = st.number_input("Customer ID", min_value=1, step=1)
        txn_type = st.selectbox("Transaction Type", ["revenue", "expense"])
        amount = st.number_input("Amount", min_value=0.0, step=100.0)
        category = st.text_input("Category")
        date = st.date_input("Transaction Date", value=datetime.now().date())
        description = st.text_area("Description")

        if st.button("Submit Transaction"):
            transaction_obj = Transaction(
                cust_id=cust_id,
                type=txn_type,
                amount=amount,
                category=category,
                date=str(date),
                description=description
            )
            result = transactionDAO.create_transaction(transaction_obj)
            st.success(f"Transaction added successfully: {result}")

    st.subheader("All Transactions")
    transactions = transactionDAO.get_all_transactions()
    if transactions:
        st.table([vars(t) for t in transactions])
    else:
        st.info("No transactions found.")

# -------------------- BUDGETS --------------------
elif menu == "Budgets":
    st.header("Budget Module")

    with st.form("add_budget"):
        cust_id = st.number_input("Customer ID", min_value=1)
        category = st.text_input("Category")
        planned_amount = st.number_input("Planned Amount", min_value=0.0)
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        submit = st.form_submit_button("Add Budget")
        if submit:
            from src.models.budget import Budget
            budget_obj = Budget(
                cust_id=cust_id,
                category=category,
                planned_amount=planned_amount,
                actual_amount=0.0,
                start_date=str(start_date),
                end_date=str(end_date)
            )
            result = budgetDAO.create_budget(budget_obj)
            st.success(f"Budget added successfully: {result}")

    st.subheader("All Budgets")
    budgets = budgetDAO.get_all_budgets()
    if budgets:
        st.table([vars(b) for b in budgets])
    else:
        st.info("No budgets found.")

# -------------------- PROFITS --------------------
elif menu == "Profits":
    st.header("Profit Module")

    cust_id = st.number_input("Customer ID for Profit Calculation", min_value=1)
    month = st.text_input("Month (YYYY-MM)")

    if st.button("Calculate Profit"):
        try:
            profit = profitDAO.calculate_profit(cust_id, month)
            st.success(f"Profit for customer {cust_id} in {month}: {profit}")
        except Exception as e:
            st.error(f"Error calculating profit: {e}")

    st.subheader("All Profits")
    profits = profitDAO.get_all_profits()
    if profits:
        st.table([vars(p) for p in profits])
    else:
        st.info("No profits found.")

# -------------------- SIMULATIONS --------------------
elif menu == "Simulations":
    st.header("Simulation Module")

    with st.form("add_simulation"):
        cust_id = st.number_input("Customer ID", min_value=1)
        scenario = st.text_input("Scenario Description")
        projected_amount = st.number_input("Projected Amount")
        submit = st.form_submit_button("Run Simulation")
        if submit:
            from src.models.simulation import Simulation
            simulation_obj = Simulation(
                cust_id=cust_id,
                scenario=scenario,
                projected_amount=projected_amount
            )
            result = simulationDAO.create_simulation(simulation_obj)
            st.success(f"Simulation added: {result}")

    st.subheader("All Simulations")
    simulations = simulationDAO.get_all_simulations()
    if simulations:
        st.table([vars(s) for s in simulations])
    else:
        st.info("No simulations found.")
