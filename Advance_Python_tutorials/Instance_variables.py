class Test:
    a=10

    def m1(self):
        self.a=15
t1=Test()
t1.m1()
print(t1.a)
print(Test.a)
