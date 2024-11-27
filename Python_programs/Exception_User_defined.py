
class my_exception(Exception):
    def __init__(self,test):
        print("age is over 100 ",end="")
    pass

try:
    num1=int(input("age 1:"))
    num2 = int(input("age 2:"))
    if num2 > 100 or num1 > 100 :
        raise my_exception("Okay")
except (my_exception) as var:
    print(var,end="")
else:
    result=num1-num2
    print("age difference is ", result)


