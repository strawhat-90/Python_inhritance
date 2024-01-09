# Write a Python program to create a class representing a bank. Include methods for
# managing customer accounts and transactions.

import random

class bank:
    
    def setdata(self):
        a=random.randint(0,10000)
        self.a=a
        
        num=int(input("\n\nEnter your Account no. : "))
        self.name=num
        
        self.choice = 0
        
        while self.choice!=4:
            
            choice=int(input("\nWhat do u want to do : \n1.Deposit money\n2.Withdrow money\n3.Check Money \n"))
            self.choice=choice
            
            if self.choice==1:
                d=int(input("HOW MUCH MONEY DO U WANT TO DEPOSIT : "))
                self.d=d
                self.getdata()
                
            elif self.choice==2:
                w=int(input("HOW MUCH MONEY DO U WANT TO Withdrow : "))
                self.w=w
                self.getdata()
                
            elif self.choice==3:
                print("U have : ")
                self.getdata()
                
            else:
                print("exit ") 
    
    def getdata(self):
        if self.choice==1:
            print(f"MONEY DEPOSIT SUCCESSFULLY...")
            print(f"u have {self.a+self.d} in your bank account ")
            self.a+=self.d
            
        elif self.choice==2:
            print(f"MONEY WITHDROW SUCCESSFULLY...")
            print(f"u have {self.a-self.w} in your bank account ")
            self.a-=self.w
            
        elif self.choice==3:
            print(self.a)  



obj=bank()
obj.setdata()
obj.getdata()       