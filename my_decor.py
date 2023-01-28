
def my_decor(add):
    def inner():
        result_of_main_func= add()
        num3 = int(input("enter third number:"))
        result=num3 + result_of_main_func
        return result
    return inner

@my_decor
def add():
    num1=int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    return num1+num2

print(add())