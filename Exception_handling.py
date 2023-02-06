num1=float(input("enter first number : "))
num2=float(input("enter second number : "))

try:
    result=num1/num2
except ZeroDivisionError:
    print(f"You can not divide by zero")

else :
    try:
       result1
    except NameError:
      print(f"Invalid Variable ",end=" ")
      print(f"Division is ", result)
    else :
      print(f"Division is ", result)
    finally:
        pass
finally:
    print("Bye")