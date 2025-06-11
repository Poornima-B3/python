class car:
    def __init__(self,Brand,color):
        self.Brand=Brand
        self.color=color
    def m1(self):
        print("Brand:",self.Brand)
        print("color:",self.color)
obj=car("BMW","Blue")            
obj.m1()




