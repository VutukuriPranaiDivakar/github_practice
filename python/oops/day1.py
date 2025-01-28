"""
Class : template for creating objects,All objects created using the same class will have the same characteristics.
object: an instance of a class.
Instantiate : create a instance of a class.
method : a function defined in a class
Attributes : a variable bound to an instance of a class
# class variable = inside the class
# instance variable == inside the functions we called instance variable
"""


class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Account created for  :: {self.name}")

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be grater than zero and no more than your account balance.")
        self.show_balance()
    
    def show_balance(self):
        print(f"Balance is {self.balance}")

if __name__ == "__main__":
    pranai = Account("Pranai", 0)
    pranai.show_balance()
    pranai.deposite(1000)
    # pranai.show_balance()
    pranai.withdraw(500)
    # pranai.show_balance()
    pranai.withdraw(12000)
    
    # pranai.show_balance() 


    