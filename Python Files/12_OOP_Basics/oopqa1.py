class BankAccount:
    def __init__(self):
        self.__balance=0
    def set_balance(self,amount):
        self.__balance+=amount
    def get_balance(self):
        print("Balance:", self.__balance)
obj=BankAccount()
obj.set_balance(1000)
obj.get_balance()

class student:
    def __init__(self):
        self.__mark=0
    def assign(self,total):
        self.__mark+=total
    def get_mark(self):
        print("Mark: ",self.__mark)
obj1=student()
obj1.assign(90)
obj1.get_mark()
   
