## Deep and Shalow copy
import copy
list1=[1,2,3,4,['A','B','C']]
## copy data
list2_shallow_copy =copy.copy(list1)

##  Deep copy data ## Allocate different memory
list3_deep_copy =copy.deepcopy(list1)

list1.append(5)
list1[0]=10000
print("original List1 : ",list1)
print("Shallow Copy : ",list2_shallow_copy)
print("Deep Copy :", list3_deep_copy)

