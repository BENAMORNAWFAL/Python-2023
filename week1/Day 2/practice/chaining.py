class User :

    def __init__(self,first_name,last_name,email,age,is_rewards_member,gold_card_points):
        self.name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.member=is_rewards_member
        self.gold=gold_card_points
        
    def display_info(self):
        print(self.name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.member)
        print(self.gold)
        return self
    def enroll(self):
        if self.member == True :
            print(self.name+' already a member ')
            self.member=False
        else:
            self.member=True

        self.gold=200
        return(self)

    def spend_points(self,amount):
        if self.gold>=amount:
            self.gold-=amount
        else:
            print(self.name+" don't have a points ")
        return(self)


user1=User('Nawfal','Benamor','technobenamor@gmail.com',29,False,0)
user2=User('Aymen','benben','aymenben@gmail.com',35,True,0)
user3=User('Mourad','Ben','mouradben@gmail.com',20,True,0)
user1.display_info().enroll().spend_points(50).display_info()
print('==================================================')
user2.display_info().enroll().spend_points(80).display_info()
print('==================================================')
user3.display_info().spend_points(40).display_info()
