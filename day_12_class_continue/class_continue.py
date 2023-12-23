class Account:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.__balance = balance

    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount {amount} deposited successfully.\nYour new balance is {self.__balance}")

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient balance")
        else: 
            self.__balance -= amount
            print(f"Amount {amount} withdrawn successfully. Your new balance is {self.__balance}")


    def get_balance(self):
        return self.__balance


account1 = Account(
    34242332432432,
    "Robert",
    balance= 2000
)


account2 = Account(
    32423543543534,
    "Ram",
    balance= 5000
)


print(account1.show_balance())
