
def sum(num1,**vararg):
    s=0
    for key in vararg:
        s= s +vararg[key]
    return s,num1
s1,n1=sum(num1=10,num2=20)
s2,n2=sum(num1=20,num2=20,num3=30)
print(f"Sum is {s1} and the first Arg is {n1} ")
print(f"Sum is {s2} and the first Arg is {n2}")