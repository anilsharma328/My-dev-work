class Test:
    def some_method(x):
        print( "some_method")
    def Add_num(a,b):
        print( a+b)

    def Multiply(a,b):
      print( a*b)

    def divide(a,b):
        print(  a/b)

    def subtract(a,b):
        print(  a-b)

t1=Test()
t1.some_method()
#Test.some_method()
Test.Add_num(2,3)
Test.Multiply(2,3)
Test.divide(2,3)
Test.subtract(2,3)
