from src.dao.transaction_dao import TransactionDAO
from src.models.transaction import Transaction

class TransactionService:
    def __init__(self):
        self.dao = TransactionDAO()

    def add_transaction(self, cust_id, type_, amount, category, date, description=""):
        transaction = Transaction(
            cust_id=cust_id,
            type=type_,
            amount=amount,
            category=category,
            date=date,
            description=description
        )
        return self.dao.create_transaction(transaction)

    def get_customer_transactions(self, cust_id):
        return self.dao.get_transactions_by_customer(cust_id)

    def get_all_transactions(self):
        return self.dao.get_all_transactions()
