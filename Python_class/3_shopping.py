# Write a Python program to create a class representing a shopping cart. Include methods for
# adding and removing items, and calculating the total price.

class shopping:
    
    def setdata(self):
        name=input("\n\nEnter the name of product : ")
        self.name=name
        
        choice=int(input("what do u want ? (1.Add product 2.Remove product)"))
        self.choice=choice
        
        if self.choice==1:
            n=int(input("How much item : "))
            self.n=n
            
        elif self.choice==2:
            r=int(input("How many items u want to remove : "))
            self.r=r
            
        else:
            print("INVALID INPUT")    

    def getdata(self):
        if self.choice==1:
            print(f"{self.n} {self.name} is added successfully ")

        elif self.choice==2:
            
            print(f"{self.r} {self.name} is remove successfully ")



obj=shopping()

obj.setdata()
obj.getdata()