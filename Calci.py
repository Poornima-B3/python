import time
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
5.exit
enter the value of your choice:"""    
choice=int(input(x))
while True:
    a=int(input("Enter the value is:"))
    b=int(input("Enter the value is:"))
    if choice==1:
        sum(a,b)
    elif choice==2:
        difference(a,b)
    elif choice==3:
        product(a,b)
    elif choice==4:
        division(a,b) 
    elif choice==5:
        break
print("Existing the caluculator")   
print()
time.sleep(2)
print("End of an application")                              