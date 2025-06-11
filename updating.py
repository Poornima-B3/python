import time
class I_HUB:
    def __init__(self):
        self.Eid=1001
    def m1(self):
        self.Eid=1002
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=I_HUB()
print() 
i1.m1()
i1.Eid=1003
print()
print("Employee_Id is:",i1.Eid)
print()
time.sleep(2) 
print("End of an appliction")      
