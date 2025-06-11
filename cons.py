import time
class car:
    def __init__(self,name,brand,year):
        self.name=name
        self.brand=brand
        self.year=year
i1=car("Benz","Fancy",2019)
print(i1.name,i1.brand,i1.year)
print()
i2=car("Toyoto","Fancy",2020)
print(i2.name,i2.brand,i2.year)
print()
time.sleep(2)
print("End of an application")        
