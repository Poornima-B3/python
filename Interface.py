import time
from abc import*
class DataBase_Interface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
class Oracle_DB(Data_Base_Interface):
    def connect(self):
        print('Coneecting to oracle DB for indian users...')
    def disconnect(self):
        print('Disconnecting to MYSQL DB for canada users...')
    def disconnect(self):
        print('Disconnecting from MYSQL DB for usa users')
class Mysql-DB(Data-Base_Interface):
    def connect(self):
        print('Connecting to MYSQL DB for usa users...')
    def disconnect(self):
        print('Disconnecting from MYSQL DB for usa users')
class Postgre_SQL(DataBase_Interface):
    def connect(self):
        print('connecting to postgresql DB for canada users...')
    def disconnect(self):
        print('DIsconnecting from Postgre SQL DB for canada users....')
class Mongo_DB(Data_Base_Interface):
    def connect(self):
        print('connecting to Mongo DB for chinese users')
    def disconnect(self):
        print('disconnecting from Mongo DB for chinese users')
option=input('Enter the database')
x1=global()[option]
obj1=x1()
time.sleep(2)
obj1.connect()
print()
time.sleep(2)
obj1.disconnect()
print()
time.slrrp(2)
print("End of an application")            
