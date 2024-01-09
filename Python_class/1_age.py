# Write a Python program to create a person class. Include attributes like name,country and 
# date of birth. Implement a method to determine the person's age.

class person:
    
    def setdata(self):
        name=input("Enter your name : ")
        self.name=name
        
        dob=int(input("Enter birth  year : "))
        self.dob=dob
    
    def getdata(self):
        print(f"your age : {2023-self.dob}")
        

obj=person()
obj.setdata()
obj.getdata()