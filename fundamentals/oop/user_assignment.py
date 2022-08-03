class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def make_transfer(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()

    def greeting(self):
        print(f"Welcome {self.name}, to your new bank account")

    def display_user_balance(self):
        print(f"Name: {self.name}, Account Balance: {self.account_balance}")



cameron = User("Cameron Bowen", "cameronbowen555@gmail.com")
guido = User("Guido Guy", "guidoguy@codingdojo.com")
monty = User("Monty Python", "montypython3@gmail.com")
nicolle = User("Nicolle Bowen", "nicolle12345@gmail.com")
michael = User("Michael Dojo", "michael@codingdojo.com")
cameron.greeting()
guido.greeting()
monty.greeting()
nicolle.greeting()
michael.greeting()

cameron.make_deposit(20000)
print(cameron.account_balance)
cameron.make_deposit(30000)
cameron.make_deposit(5234)
cameron.make_withdrawl(100)
print(cameron.account_balance)

guido.make_deposit(500)
guido.make_deposit(4525)
print(guido.account_balance)
guido.make_withdrawl(300)
print(guido.account_balance)
guido.make_withdrawl(500)

monty.make_deposit(6000)
print(monty.account_balance)
monty.make_withdrawl(200)
monty.make_withdrawl(500)
monty.make_withdrawl(1000)
print(monty.account_balance)

nicolle.make_deposit(500)
print(nicolle.account_balance)

michael.make_deposit(400)
print(michael.account_balance)

cameron.display_user_balance()
guido.display_user_balance()
monty.display_user_balance()
nicolle.display_user_balance()
michael.display_user_balance()

cameron.make_transfer(500, nicolle)
