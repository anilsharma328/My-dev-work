class A:
    def __init__(self):
        self.__x=10
    def ___m1(self):
        print("this is a private member")


t=A()
print(t._A__x)
print(t._A___m1())
