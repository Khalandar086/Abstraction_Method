

from abc import ABC,abstractmethod
class Rbi(ABC):
    @abstractmethod
    def bank_name(self):
        pass
    def interest(self):
        pass
    def account_type(self):
        pass
    def loan(self):
        print('All types of loan facility available in this bank')

    def authorization(self):
        print("This is authorised bank of RBI")
        print(isinstance(self,Rbi))

class Sbi(Rbi):
    def bank_name(self):
        print('This is Sbi Bank')
    def interest(self):
        print("Sbi gives 10% interest")

    def account_type(self):
        print('SBI Provides All Types Of Accounts')

class Axis_Bank(Rbi):
    def bank_name(self):
        print('This is Axis Bank')

    def interest(self):
        print('Axis Bank gives 5% interest')

    def account_type(self):
        print('Axis Bank Provides Savings and Current Accounts')

    def loan(self):
        print('loan facility is not available in these Bank')
class Indian_Bank(Rbi):
    def bank_name(self):
        print('This is a Indian_Bank')


    def interest(self):
        print('Indian_Bank gives 15% interest')

    def account_type(self):
        print('Indian_Bank Provides Savings,Current and Fixed Accounts')


s=Sbi()
i=Indian_Bank()
a=Axis_Bank()
s.bank_name()
s.account_type()
s.interest()
s.loan()
s.authorization()
print('_______')
i.bank_name()
i.account_type()
i.loan()
i.authorization()