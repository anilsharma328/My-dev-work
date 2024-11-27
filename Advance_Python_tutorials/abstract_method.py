from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
       ## child class must provide defination for abstarct method 
    def getwheelsInfo():
        pass


class van(vehicle):
    def getwheelsInfo(self):
        return "number of wheels are",6

class Auto(vehicle):
     '''pass '''  
     def getwheelsInfo(self):
        return "number of wheels are",3
 

v=van()
print(v.getwheelsInfo())

A=Auto()
print(A.getwheelsInfo())
