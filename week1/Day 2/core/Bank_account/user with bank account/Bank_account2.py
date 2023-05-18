class BankAccount:
    
    bank_name='zitouna'
    def __init__(self,name): #the information account
        self.name=name
        self.int_rate=0.01
        self.balance=500
        
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
   
        
