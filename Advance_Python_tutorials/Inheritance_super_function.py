class P:
    def __init__(self):
        print("Parent class constructor")

    a=100

    def m1(self):
        print("Instance Method")

    @classmethod
    def m2(cls):
        print("class method")
    @staticmethod
    def m3():
        print("this is a static method")



        
    
class C(P):
    def __init__(self):
       print("child class constructor")
    def method(self):
        print(" Value of a is ", super().a)
        super().m1()
        super().m2()
        super().m3()
        super().__init__()
child=C()
child.method()
