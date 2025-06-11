import time
class I_HUB:
    def __init__(self):
        self.Eid=1001
        self.Ename="Poornima"
        self.Esal=34000
        print(self.Eid,self.Ename,self.Esal)
    def m1(self):
        self.Design="Python Developer"
        self.company="accenture"
        print(self.Design,self.company)
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=I_HUB()
print()
i1.m1()
print()
i1.city="Banguluru"
i1.state="karknataka"
i1.country="India"
print(i1.city,i1.state,i1.country) 
print()
time.sleep(2)
print("End of an application")
                   