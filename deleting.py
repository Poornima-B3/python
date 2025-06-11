import time
class Teachers:
    def __init__(self):
        self.Tid=10022
        self.Tname="visala Lakshmi"
        self.Tsubject="English"
        del self.Tname
        del self.Tid
    def m1(self):
        self.Tcourse="PH.D"
        self.Tvillage="Narasaraopet"
        self.Tfav="Blue"
        del self.Tcourse
        del self.Tfav
    @classmethod
    def m2(cls):
        pass
    @staticmethod 
    def m3():
        pass
i1=Teachers()
print(i1.__dict__)
print()
i1.m1()
print()
print(i1.__dict__)
print()
i1.state="Andhra pradesh"
i1.country="India"
i1.city="Vijayawada"
del i1.state
del i1.country 
print()
print(i1.__dict__)
print()
time.sleep(2)
print("End of an application")          