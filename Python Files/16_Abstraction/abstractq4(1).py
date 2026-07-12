from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def interest_rate(self):
        pass

class SBI(Bank):

    def interest_rate(self):
        print("SBI Interest Rate = 6.5%")

class HDFC(Bank):

    def interest_rate(self):
        print("HDFC Interest Rate = 7.0%")

s = SBI()
s.interest_rate()

h = HDFC()
h.interest_rate()