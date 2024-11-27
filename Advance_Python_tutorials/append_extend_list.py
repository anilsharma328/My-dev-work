##  extend and append method
##  extend : add multiple element in list
## append : add only one element in the list
list1=[0,2,3,4,5,"test"]
list2=[["hello",2,4],1]
tuple1=(21,32,"holla",21)
list1.extend(list2)
list1.extend(tuple1)

list1.append("Anil ")

#tuple2=tuple1.extend(list1)  ## extend is not supported
print (list1)

