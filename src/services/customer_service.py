from src.dao.customer_dao import CustomerDAO
from src.models.customer import Customer

class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDAO()

    def add_customer(self, name, email, phone, city=None):
        customer = Customer(name=name, email=email, phone=phone, city=city)
        return self.customer_dao.create_customer(customer)

    def list_customers(self):
        return self.customer_dao.get_all_customers()

    def find_customer(self, cust_id: int):
        return self.customer_dao.get_customer_by_id(cust_id)

    def remove_customer(self, cust_id: int):
        return self.customer_dao.delete_customer(cust_id)
