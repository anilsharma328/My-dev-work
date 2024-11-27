###  Class /Instance ,clas and instance method/objects 

class Test:
    message="Hello, Welcome "  ##  Static Variable 
    def __init__(self,name):
        self.name=name  ##  Instance Variable 

    def display(self):  ##  Instance Method 
        print(self.name)

    @staticmethod
    def  Test_static():
        print(Test.message," from Static Method")

    @classmethod
    def Test_classmethod(clss):
        print(clss.message, " from Class Method")
        

T1=Test('Anil')
T2=Test('Shikha')

Test.Test_static()
Test.Test_classmethod()

T1.display()
T2.display()

print(Test.message," from outside of class defination")

'''

Output: 
Hello, Welcome   from Static Method
Hello, Welcome   from Class Method
Anil
Shikha
Hello, Welcome   from outside of class defination
'''