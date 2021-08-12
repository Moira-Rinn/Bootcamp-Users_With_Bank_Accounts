class User:
    acct = []

    def __init__(self, name, age, dob, email):
        self.name = name
        self.age = age
        self.dob = dob
        self.email = email
        User.acct.append(Bank(int_rate=0.02, balance=0))

    def make_deposit(self, x, amount):
        return User.acct[x].deposit(amount)

    def make_withdral(self, x, amount):
        return self.acct[x].withdraw(amount)

    def display_user_balance(self, x):
        return self.acct[x].display_acct_balance()

    def transfer_money(self, x, amount, y, other_user):
        self.acct[x].withdraw(amount)
        other_user.acct[y].deposit(amount)
        return self

    def open_account(self):
        User.acct.append(Bank(int_rate=0.02, balance=0))


class Bank:
    bank_name = 'Liberation Cooperative'
    all_accounts = []

    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.int_rate = int_rate
        Bank.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_acct_balance(self):
        return f"Balance: ${round(self.balance, 2)}\n"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate

    def create_account(amount):
        return f"acct_{str(Bank.acct_num)}"

    @classmethod
    def all_balances(cls):
        for acct in cls.all_accounts:
            print(Bank.display_acct_balance(acct))

    @classmethod
    def all_info(cls):
        acct_num = 1
        for acct in cls.all_accounts:
            print(
                f"{cls.bank_name}\nacct_{acct_num}:\n{Bank.display_acct_balance(acct)}")
            acct_num += 1


sara = User("Sara McCloud", 27, "July 19th, 1994", "SMcCloud@gmail.com")
rachael = User("Rachael Anderson", 19, "October 31st, 2002",
               "RAnderson@hotmail.com")
liz = User("Elibeth McKnight", 43, "March 23rd, 1978",
           "EMcKnight@gmail.com")

sara.make_deposit(0, 1000)
print(sara.display_user_balance(0))
sara.open_account()
print(sara.display_user_balance(1))


liz.make_deposit(10000)
print(liz.display_user_balance())

liz.transfer_money(sara, 2000)
print(sara.display_user_balance())
print(liz.display_user_balance())
