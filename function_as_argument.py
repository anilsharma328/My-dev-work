

def first_function():
    print("Hello, I am first function")

def second_function(ff):
    print("Hello, I am second function")
    ff()

second_function(first_function)

def bonus():
    b=1000
    return b

def Total_salary(bonus_amt):
    Base=20000
    print(f"bonus is : { bonus_amt() }")
    print(f"Total salary is : {Base  + bonus_amt()  }")
b1=bonus
Total_salary(b1)


