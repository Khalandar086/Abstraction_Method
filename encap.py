class  Bank_Customer:
    def __init__(self, account_no,balance,phone_no,address):
        self.account_no=account_no
        self.__balance=balance
        self.phone_no=phone_no
        self.address=address
    def get_balance(self):
        print(self.__balance)

    def set_deposit(self,balance,acc_type):
        if acc_type=='saving':
            self.__balance=self.__balance+balance
            print(self.__balance)
        elif acc_type=='current':
            self.__balance=self.__balance+balance
            print(self.__balance)
        else:
            raise TypeError ("Deposit type not exits")

    def set_withdraw(self,balance):
        if balance<Customer_1.__balance:
            self.__balance=self.__balance-balance
            print(self.__balance)
        else:
            print('insufficient Balance')


Customer_1=Bank_Customer(101,5000,78945612300,'atp')
print(Customer_1._Bank_Customer__balance)
Customer_1.set_deposit(100,'saving')
Customer_1.set_withdraw(600)
Customer_1.set_withdraw(500)
Customer_1.get_balance()
Customer_1.set_deposit(100,'savg')