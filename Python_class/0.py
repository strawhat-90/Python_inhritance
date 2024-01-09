class shape:
    def __init__(self):
        self.l = None
        self.b = None


    def getdata(self):

        if (self.b==None):
            print(self.l*self.l)
        else:
            print(self.l*self.b)    
        
    
class area(shape):
    def setdata(self):
        c=int(input("1.squre 2.rectangle"))
        if c==1:
            self.l=int(input("Enter the length :  "))
        elif c==2:
            self.l=int(input("Enter the length :  "))
            self.b=int(input("Enter the bredth :  "))
        else:
            print("INVLAID INPUT")    
            

obj=area()
obj.setdata()
obj.getdata()