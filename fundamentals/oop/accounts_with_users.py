class BankAccount:
    account_type = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account_type.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance-amount) >= 0:
            self.balance -= amount
        else:
            print(f"Insufficent Funds, charging 5$ fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        return f"{self.balance}"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def display_all_account_type(cls):
        for account_type in cls.account_type:
            account_type.display_account_info()


class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(.05,10000)

    def display_user_balance(self):
        print(f" Name: {self.name}, Account Balance: {self.account.display_account_info()}")
        return self

    def make_transfer(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


cameron = User("Cameron Bowen")

cameron.account.deposit(5000)

cameron.display_user_balance()