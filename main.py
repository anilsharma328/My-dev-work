"""
# Prime Number
number=int(input("enter number:"))
print("you have entered : ",number)

for i in range(2,number):
    if number % i==0:
        print("Not a prime number",number,i)
        break
else:
        print("Prime number", number, i)



def person(name,age=22):
    print(name)
    print(age)

person("anil")

def person(*name):
    #print(name)
    for i in name:
        print (i)
person("anil","Sharma",123)

tup1=(1,'test','name','test')
tup1[1]='No test'
print (tup1)




dic1={  "apple" :1,
        'banana' :2 ,
        'Orange' :3

}

dic2 ={
    'watermellon' :4,
    'neembo' :5

}

dic3=dic1.copy()
dic3.update(dic2)
dic3.pop('neembo')
print (dic3)

"""


set={'test','maths','test' }
set.add('english')
set.add('english')
print(set)