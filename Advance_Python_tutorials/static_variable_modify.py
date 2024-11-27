class Test:
    a=10
    def __init__(self):
        Test.a=30
    def m1(self):
        Test.a=40
    @classmethod
    def m2(cls):
        cls.a=50
    @staticmethod
    def m3():
        Test.a=60

t=Test()
t.m1() ## calling using object
Test.m2() ## you can call using classname of object reference
Test.m3()
Test.a=70
print(Test.a)
