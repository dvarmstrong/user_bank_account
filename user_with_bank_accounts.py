class User:

    def __init__(self, name): 
        # assign them accordingly 
        self.name = name
        self.account = {
            "checking" : BankAccount(0.02,1000),
            "savings" : BankAccount(.05, 3000)
        }
    
        
    
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawl(self, amount):
        if (self.balance -amount) >= 0:
            self.balance -= amount
        else:
            self.balance -= 5
            print (f"{User}insufficient funds! Charging $5 fee")
        
    
    def display_account_info(self):
        return f"{self.balance}"
        

    def yield_intrest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for accounts in cls.accounts:
            accounts.display_account_info()
            



dimitri = User('dimitri')
maggie = User('maggie')
tom = User('tom')

dimitri.account['checking'].deposit(100)
dimitri.display_user_balance()

maggie.display_user_balance()
maggie.account['savings'].deposit(5000)
maggie.display_user_balance()
dimitri.account['checking'].withdrawl(5000)
dimitri.account['checking'].display_account_info()
