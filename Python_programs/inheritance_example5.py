class A:
    def m1(self):
        print("this is method A")

class B(A):
    pass
    #def m1(self):
    #    print("this is method D")

class C(A):
    def m1(self):
        print("this is method C")

class D(B,C):
    pass
    #def m1(self):
    #    print("this is method D")

d=D()
d.m1()
