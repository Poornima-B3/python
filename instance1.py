import time
class Employees:
    def __init__(self,Eid,Ename,Esal,Design,company):
        self.Eid=int(input("Enter the Eid:"))
        self.Ename=input("Enter the Ename:")
        self.Esal=float("Enter the Esal:")
        self.Design=input("Enter the Design:")
        self.company=input("Enter the company")
    def m1(self):
        print("--------Employee_Informaion-----")    
        print('Eid is:',self.Eid)
        print("Ename is:",self.Ename)
        print("Esal is:",self.Esal)
        print("Design is:",self.Design)
        print("company is:",self.company)
        print("------------------------")
e1=Employees(Eid=None,Ename=None,Esal=None,Design=None,company=None)
print()
e1.m1()
print()
time.sleep(2)
print("End of an application")        