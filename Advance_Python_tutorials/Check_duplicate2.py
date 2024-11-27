
#### check duplicate elemenntsin the list
list1=["Anil","Sharma","Bhopal","Mumbai","Anil","Thane","Bhopal"]
duplicate=[]
for ele in range(len(list1)):
    for next_ele in  range(ele +1 ,len(list1)):
        if list1[ele]==list1[next_ele] :
            duplicate.append(list1[ele])

print(duplicate)

