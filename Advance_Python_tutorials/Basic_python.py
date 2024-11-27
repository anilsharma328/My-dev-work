

"Dictionary "

d1={"Anil" :2000
,"Shikha" :300
,"Jyotsna": 10000
}
""""
d1["Sunil"]=200000
print(d1)
d2=d1.copy()
del d1["Sunil"]
print("d1",d1)
print("d2",d2)

d2.update({"Jyotsna": 30000})
print("d2 after update",d2)

print (d2.keys())  #print Keys
print (d2.items())  #Print Key value Pair

d1.clear()
print(d1)
"""
#del d1["Anil"]
#print(d1)
#print(type(d1))


#####  keywords Arguments

def test(**args):
    print("Argumnets are: ",args)

    print(type(args))
test(a=1,b=2,c=2,d=2 )
#test()




