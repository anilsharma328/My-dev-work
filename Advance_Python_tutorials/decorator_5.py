
def square_square_decor1(func1):
    def inner1(num):
        x=func1(num) *func1(num)
        print("Square decor output is :",x)
    return inner1

    
def double_decor2(func2):
    def inner2(num):
        x=func2(num) * 2
        print("Double decor output is :" ,x)
        return x
    return inner2        

@square_square_decor1
@double_decor2
def f1(num):
    print("Num passed",num)
    return num

print("*" *30)
f1(2)
print("*" *30)
f1(10)

print("*" *30)
