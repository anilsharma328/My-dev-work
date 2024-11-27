
stack=[]
def add_element():
    val = input("element to be added : ")
    print("Before:", stack)
    stack.append(val)
    print("After:", stack)



def remove_element():
    print("Before:", stack)
    stack.pop()
    print("After:", stack)


while True:
    print("select operation 1. push 2.Pop 3.quit")
    user_operation= int(input())
    if user_operation==1:
        add_element()
    if user_operation== 2:
        if len(stack) >0:
            remove_element()
        else:
            print("No element present")
            pass
    if user_operation== 3:
        exit()
