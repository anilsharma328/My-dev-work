a=10
def test():
    print("Hello")
    b=100
    print(locals()['b'])
    print("before update",a)
    globals()['a'] =1000

test()
print("After update",a)