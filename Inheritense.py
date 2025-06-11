#single inheritence
class Parent:
    def fun1(self):
        print("This is Parent class")
class child:
    def fun2(self):
        print("This is child class") 
obj=child()
obj.fun2()

# multilevel inheritence:
class Parent:
    def fun1(self):
        print("This is Parent class")
class child(Parent):    
    def fun2(self):
        print("This is child class")
class grandchild(child):
    def fun3(self):
        print("This is grandchild class")
obj=grandchild()
obj.fun1() 
obj.fun2()
obj.fun3()          

#Hierachicl inheritense
class Parent:
    def fun1(self):
        print("This is Parent class")
class child1(Parent):
    def fun2(self):
        print("This is child1 class")
class child2(Parent):
    def fun3(self):
        print("This is child2 class")
obj=child2()
obj.fun1()

#Mutilevel Inheritence:
class father:
    def fun1(self):
        print("This is father class")
class mother:
    def fun2(self):
        print("This is mother class")
class child(father,mother):
    def fun3(self):
        print("This is child class")
obj=child()
obj.fun1()
obj.fun2()
obj.fun3()                

