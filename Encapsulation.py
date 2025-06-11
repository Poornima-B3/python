'''
Wrapping of variables methods in a single unit is called Encapsulation
Public
Private __
Protected _
'''
class demo():
    def __init__(self,a,b):
        self.__a=a #prvate
        self._b=b #protected
class demo2(demo):
    def output(self):
        print(self._b)
d=demo2(3,4)
d.output()        



#Polymorphism

def add(a,b):
    print(a+b)
add(1,2)
add('a','b')
add([3,4],[5,6])
add((3,4),(6,7))    

