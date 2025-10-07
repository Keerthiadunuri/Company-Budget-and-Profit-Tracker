class Customer:
    def __init__(self, cust_id=None, name=None, email=None, phone=None, city=None):
        self.cust_id = cust_id
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city

    def __repr__(self):
        return f"<Customer {self.cust_id}: {self.name}, {self.email}, {self.phone}, {self.city}>"
