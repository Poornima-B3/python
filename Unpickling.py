import time
import pickle
class Train_Information:
    def __init__(self,tno,tname,arrtime,depttime,date,source,destination):
        self.tno=tno
        self.tname=tname
        self.arrtime=arrtime
        self.depttime=depttime
        self.date=date
        self.source=source
        self.destination=destination
    def m1(self):
        print("=====Train_Information=======")
        print("tno is:",self.tno)
        print("tname is:",self.tname)
        print("arrtime is:",self.arrtime)
        print("depttime is:",self.depttime)
        print("date is :",self.date)
        print("source is:",self.source)
        print("destination is:",self.destination)
print()
print("====Welcome to IHub for  Unpickling in python======")
with open("A.txt","rb")as f:
    t1=Train_Information(12345,"Palnadu Express","11:00 AM","4:00 PM","10/5/2025","pa","Narasaaopet")  
    s=pickle.load(f)
    s.m1()
    print()
    print("Unpickling is done succsfully.....")




