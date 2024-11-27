
#max and min element from array#
list1=[21,21,23,43,2,54,65,32,25,4,5,0.11,1000,43,21]
max = list1[0]
min = list1[0]
for i in range(len(list1)):
    if list1[i] > max:
        max =list1[i]
    elif list1[i] < min:
        min =list1[i]

print(max,min)