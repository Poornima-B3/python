import time
class teachers:
    def __init__(self,name,age,email,address):
        self.name=name
        self.age=age
        self.email=email
        self.address=address
    def m1(self):
        print("name:",self.name)
        print("age:",self.age)
        print("email:",self.email)
        print("address:",self.address)
        print("------------------------")
obj=teachers("Venakteswarlu",33,"venkibailadugu@gmail.com","Narasaraopet")
obj.m1()
obj2=teachers("Poornima",27,"poornima131416@gmail.com","Narasaraopet") 
obj2.m1()
obj3=teachers("Keerthi",25,"keerthi14@gmail.com","Narasaraopet") 
obj3.m1()
obj4=teachers("Divya",22,"divya16@gmail.com","Narasaraopet") 
obj4.m1()
       
       
