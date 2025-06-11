class a:
    def __init__(self,base):
        self.base=base
    class b:
        def __init__(self,height,base):
            self.base=base
            self.height=height
        def m1(self):
            print('area of the triangle is: ',0.5*self.base*self.height)
obj=a(2)
m=obj.b(7,obj.base)
m.m1()
