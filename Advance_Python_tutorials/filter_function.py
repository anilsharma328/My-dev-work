
list1=[10,11,12,13,14,15,16]
def check_even(num):
    if num % 2 ==0:
        return "even",num
result_set=list(filter(check_even,list1))
#result_set=filter(check_even,list1)
print(result_set)
