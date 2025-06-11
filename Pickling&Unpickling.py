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
        print("tno is:",tno)
        print("tname is:",tname)
        print("arrtime is:",arrtime)
        print("depttime is:",depttime)
        print("date is :",date)
        print("source is:",source)
        print("destination is:",destination)
    print()
print("====Welcome to IHub for  pickling in python======")
with open("A.txt","wb")as f:
    t1=Train_Information(12345,"Palnadu Express",11:00 AM,4:00 PM,10/5/2025,pa,"Narasaaopet")   
    pickle.dump(t1,f)
    print()
    print("Pickling process is done")
print()
time.sleep(2)
print("End of an application")                


