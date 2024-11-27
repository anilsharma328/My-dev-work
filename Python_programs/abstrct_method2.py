from abc import *

class A(ABC):
    def non_ABS_method(self):
        print("this is non-abstract method")
    @abstractmethod
    def my_method(self):
        pass

class B(A): 
    def my_method(self):
        print("this is abstract menthod")
b=B()
b.my_method()
b.non_ABS_method()
