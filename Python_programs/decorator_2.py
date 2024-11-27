list1=[1,2,3,4,5,6,7,8,9,10]

def check_odd(to_check):
        if to_check%2 !=0:
            return True
            #pass
        else:
            return False
        

list2=list(filter(check_odd,list1))
#for i in list2: print (i)

print(list2)
