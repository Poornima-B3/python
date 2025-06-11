import time
class I_HUB:
    def __init__(self):
        self.Eid=1001
        self.EName="Poornima"
        self.Esal=34000
    def m1(self):
        self.Design="Python Developer"
        self.Company="Infosys"
        self.Doj="13/05/2025"
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=I_HUB()
print(i1.__dict__)
print()
i1.m1()
print(i1.__dict__)
print()
i1.city="Hyderabad"
i1.state="Telangana"
i1.country="India"
print()
print(i1.__dict__)
time.sleep(2)
print("End of an application")
