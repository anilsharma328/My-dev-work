def outer():
    print("this is outer function")
    def inner():
        print("this is inner function")
    return inner

innner_ret=outer()
innner_ret()

#passing function as an argument to another function 

def f1(funcq):
    print("this is f1 function")
    funcq()

def f2():
    print("this is f2 function")

f1(f2)
