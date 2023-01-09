import shelve
from User import User


class Customer(User):
    with shelve.open("Customers") as customers:
        count = len(customers)

    def __init__(self, firstname, lastname, gender, membership, remarks, email, joindate, address):
        super().__init__(firstname, lastname, gender, membership, remarks)
        self.__customerid = str(Customer.count)
        Customer.count += 1
        self.__email = email
        self.__joindate = joindate
        self.__address = address

    def get_customerid(self):
        return self.__customerid
    
    def get_joindate(self):
        return self.__joindate

    def get_email(self):
        return self.__email
    
    def get_address(self):
        return self.__address

    def set_customerid(self, customerid):
        self.__customerid = customerid
    
    def set_email(self, email):
        self.__email = email
    
    def set_joindate(self, joindate):
        self.__joindate = joindate

    def set_address(self, address):
        self.__address = address
    
