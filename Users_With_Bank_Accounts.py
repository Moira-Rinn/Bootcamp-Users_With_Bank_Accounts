class User:
    def __init__(self, name, age, dob, email):
        self.name = name
        self.age = age
        self.dob = dob
        self.email = email
        self.account = Bank(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        return self.account.deposit(amount)

    def make_withdral(self, amount):
        return self.account.withdraw(amount)

    def display_user_balance(self):
        return self.account.display_acct_balance()

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

    def open_account(self, amount):
        self.account.create_account(amount)


class Bank:
    bank_name = 'Liberation Cooperative'
    all_accounts = []
    acct_num = 1

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

        Bank.all_accounts.append(f"acct_"{str(Bank.acct_num)})
        Bank.acct_num += 1

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

sara.make_deposit(1000)
print(sara.display_user_balance())

liz.make_deposit(10000)
print(liz.display_user_balance())

liz.transfer_money(sara, 2000)
print(sara.display_user_balance())
print(liz.display_user_balance())
