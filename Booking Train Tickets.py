import random
class train:
    def __init__(self,bill=0,name='',age=0,gender='',e=0,g=0,h=0):
        print(" **************WELCOME TO KATPADI JUNCTION***************")
        self.bill=bill
        self.name=name
        self.age=age
        self.gender=gender
        self.e=e
        self.g=g
        self.h=h
        
    def chuma(self):
        c=input("STARTING PLACE:")
        t=input("DESTINATION:")
        print("the available trains are   1.150986 2.134567")
        print("choose 1 for 5 am")
        print("choose 2 for 3 pm")
        d=int(input("enter your choice:"))
        self.p1=[]
        self.r1=[]
        self.s1=[]
        
        if d==1 or d==2:
            self.e=int(input("NO OF PASSENGERS:"))
            self.g=int(input("NO OF ADULTS:"))
            self.h=int(input("NO OF CHILDREN:"))
            for i in range(1,self.e+1,1):
                p=input("ENTER PASSENGER NAMES:")
                self.p1.append(p)
                r=input("GENDER:")
                self.r1.append(r)
                s=int(input("AGE:"))
                self.s1.append(s)
                
            print(" ")
            print("1 for class A")
            print("2 for class B ")
            f=int(input("enter the class:"))
            if f==1:
                print("YOU HAVE CHOSEN CLASS A")
                self.bill=(1500*self.g)+(1000*self.h)
                
            else:
                print("YOU HAVE CHOSEN CLASS B")
                self.bill=(1000*self.g)+(500*self.h)
                
        else:
            print("enter the valid option")
    def display(self):
        x=0
        for i in range(1,self.e+1):
            print("Name of the Passenger:",self.p1[x])
            print("Gender:",self.r1[x])
            print("Age:",self.s1[x])
            print("The Ticket Amount is:",self.bill)
            x+=1
        
class bye(train):
    def byee(self):
        print("THANK YOU")
        print("VISIT US AGAIN")
z=bye()
z.chuma()
z.display()
z.byee()
            
            
        
        
