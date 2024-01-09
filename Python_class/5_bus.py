# Create a Bus child class that inherits from the Vehicle class. The default fare
# charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we
# need to add an extra 10% on full fare as a maintenance charge. So total fare for
# bus instance will become the final amount = total fare + 10% of the total fare.

class vehical:
    def __init__(self):
        self.bus=15
    
    def setdata(self):
        
        choice=int(input("what's your vehicla seat capacity : \n1. 2 seater\n2. 4 seater\n3. 5 seater\n4. Bus or truck like vehical\n\n "))
        self.choice=choice

class bus(vehical):
    def getdata(self):
        if self.choice==1:
            print(f"u have to pay : RS{2*100}")
        elif self.choice==2:
            print(f"u have to pay : RS{4*100}")    
        elif self.choice==3:
            print(f"u have to pay : RS{5*100}")
        elif self.choice==4:
            print("your vehical is bus or truck type SO, u have to pay 10% maintenance")
            print(f"SO, u have to pay : RS{(self.bus*100)+150}")
        else :
            print("INVALID CHOICE") 

obj=bus()
obj.setdata()
obj.getdata()