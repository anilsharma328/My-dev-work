
string1=')) (('

counter=0

def checker(string,counter):
    for i in string:
        if i=='(':
            counter=counter+1
        elif i==')':
            counter=counter-1
        
    return counter

if checker(string1,counter)==0 :
    print("Balanced")
elif checker(string1,counter)<0 :
    print(" ) not opened")
elif checker(string1,counter)>0 :
    print("( not closed")
