import time
a=int(input("Enter the value is:"))
b=int(input("Enter the value is:"))
def sum(a,b):
    print(a+b)
def difference(a,b):
    print(a-b)
def product(a,b):
    print(a*b)
def division(a,b):
    print(a/b)
x="""1.sum
2.difference
3.product
4.division
enter the value of your choice:"""    
choice=int(input(x))
if choice==1:
    sum(a,b)
if choice==2:
    difference(a,b)
if choice==3:
    product(a,b)
if choice==4:
    division(a,b)
print()
time.sleep(2)
print("End of an application")                              