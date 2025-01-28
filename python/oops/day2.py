import datetime
import pytz

class Account:
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print(f"Account created for :: {self.name}")

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))  

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))  
        else:
            print("The amount must be greater than zero and no more than your account balance.")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.balance}")

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = "Deposited"
            else:
                trans_type = "Withdrawn"
                amount *= -1
            local_time = date.astimezone(pytz.timezone("Asia/Kolkata"))  
            print("{:6} {} on {} (local time was {})".format(amount, trans_type, date, local_time))

if __name__ == "__main__":
    pranai = Account("Pranai", 0)
    pranai.show_balance()
    pranai.deposite(1000)
    pranai.withdraw(500)
    pranai.withdraw(12000)
    pranai.show_transaction()

    divakar = Account("Divakar", 1000)
    divakar.show_balance()
    divakar.deposite(100)
    divakar.withdraw(250)
    divakar.show_transaction()