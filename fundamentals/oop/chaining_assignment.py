class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def make_transfer(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

    def greeting(self):
        print(f"Welcome {self.name}, to your new bank account")
        return self

    def display_user_balance(self):
        print(f"Name: {self.name}, Account Balance: {self.account_balance}")
        return self



cameron = User("Cameron Bowen", "cameronbowen555@gmail.com")
guido = User("Guido Guy", "guidoguy@codingdojo.com")
monty = User("Monty Python", "montypython3@gmail.com")
nicolle = User("Nicolle Bowen", "nicolle12345@gmail.com")
michael = User("Michael Dojo", "michael@codingdojo.com")
cameron.greeting()


cameron.greeting().make_deposit(20000).make_deposit(30000).make_deposit(5234).make_withdrawl(100).make_transfer(500, nicolle).display_user_balance()



guido.greeting().make_deposit(500).make_deposit(4525).make_withdrawl(300).make_withdrawl(500).display_user_balance()


monty.greeting().make_deposit(6000).make_withdrawl(200).make_withdrawl(500).make_withdrawl(1000).display_user_balance()


nicolle.greeting().make_deposit(500).display_user_balance()


michael.greeting().make_deposit(400).display_user_balance()


