from Bank_account2 import BankAccount

class User(BankAccount):
    def __init__(self,name,int_rate,balance):
        super().__init__(self)
        self.name=name
        self.int_rate=int_rate
        self.balance=balance


    def make_deposit(self, amount):
        super().deposit(amount)
        print('an other deposit')
        
    
    def make_withdrawal(self, amount):
        super().withdraw(amount)
        print('an other decreases')
    
    def display_user_balance(self):
        print(f'Your balance now is {self.balance}')

    def choose_user(self,x,choose,money):
        
        ch=['AAA','BBB','CCC','DDD']
        ch1=[user1,user2,user3,user4]
        for i in range(0,len(ch)):
            if ch[i]==x:
                user=ch1[i]
        
        if choose=='withdrawing':
            user.make_withdrawal(int(money))
            user.display_user_balance()
            
        elif choose=='depositing':
            user.make_deposit(int(money))
            user.display_user_balance()
        else: print('your choose false')
                
            

    
        


user1=User("AAA",0.02,30000)
user2=User("BBB",0.02,14000)
user3=User("CCC",0.02,2000)
user4=User("DDD",0.02,35000)
user=User('sss',0.03,300)
x=input("choose your name account :")

choose=input('please choose if withdrawing or depositing:')

        

money=input('put your money withdrawing / depositing :')
user.choose_user(x,choose,money)




