
def my_decor(Add_func_pass):  ###Pass original function reference

    def my_inner_func(x,y):    ###working as a function
        if x%2==0 & y %2==0 :  ## checks if we need to run decorator 
            print("@"*30)
            print("Both are even numbers and Sum of numbers is :",end ="")
            Add_func_pass(x,y)
            print("@"*30)
        else:
            Add_func_pass(x,y)   ### run original function for non decorator 
    return my_inner_func
    
@my_decor    
def Add_func(a,b):
    print( a+b)
######  Simple function/ without decorator

Add_func(2,30)
Add_func(5,25)
