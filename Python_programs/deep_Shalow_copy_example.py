## Deep and Shalow copy
import copy
list1=[1,2,3,4]
list2_shallow_copy =copy.copy(list1)
list3_deep_copy =copy.deepcopy(list1)
list1.append(5)
list1[0]=10000
print(list1)
print(list2_shallow_copy)
print(list3_deep_copy)
