

try:
    age = int(input("enter your age : "))
    if age <0:
        raise ValueError("invalid age ")
    print ("your age is ",age)
except ValueError as var:
    print(var )




