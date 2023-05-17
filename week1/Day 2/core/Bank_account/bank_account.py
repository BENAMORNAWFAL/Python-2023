class BankAccount:
    
    bank_name='zitouna'
    def __init__(self,name, int_rate, balance): #the information account
        self.name=name
        self.int_rate=int_rate
        self.balance=balance
        
    def deposit(self, amount): #increases the account balance by the given amount
        self.balance+=amount
        return self
    def withdraw(self, amount): #decreases the account balance by the given amount
        if self.balance>=amount:
            self.balance-=amount
            return self
        else: 
            print('Insufficient funds: Charging a $5 fee')
            self.balance-=5
            return self
    
    def display_account_info(self): # display the information account
        print(f'{self.name} have a {self.int_rate} interest rate')
        print(f'{self.name} have a {self.balance} $')
    
       

    def yield_interest(self): # increases the account balance by the current balance * the interest rate
        self.balance+=self.balance*self.int_rate
        return self
   
        
        
    

user1=BankAccount('AAA',0.01,500)
user2=BankAccount('BBB',0.01,1000)
user3=BankAccount('CCC',0.01,450)
user1.deposit(50).deposit(80).deposit(30).withdraw(60).yield_interest().display_account_info()
user2.deposit(300).deposit(100).withdraw(40).withdraw(100).withdraw(30).withdraw(15).yield_interest().display_account_info()

