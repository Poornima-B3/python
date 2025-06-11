import time
from abc import*
class I_HUB_IT:
    @abstractmethod
    def m1(self):
        pass
i1=I_HUB_IT() 
i1.m1()
print()
time.sleep(2) 
print("End of an application")      