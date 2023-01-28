
def outer():
    a=100
    def inner():
        return "hello I am inner function"
    return a,inner
x,y=outer()
print(f"returnd value is {x} and :  {y()}")