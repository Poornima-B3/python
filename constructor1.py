import time
class Employees:
    def __init__(self):
        self.Eid=1001
        self.Ename="Poornima"
        self.Esal=45000
        self.Design="Python Developer"
        self.company="Infosys"
    def m1(self):
        print("----Employees Information-----")
        print('Eid is:',self.Eid)
        print("Ename is:",self.Ename)
        print("Esal is:",self.Esal)
        print("Design is:",self.Design)
        print("company is:",self.company)
        print("-------------------------") 
print()
e1=Employees()
e1.m1()
print()
time.sleep(2)
print("End of an application")        
