#### check duplicate elemenntsin the list 
list1=["Anil","Sharma","Bhopal","Mumbai","Anil","Thane","Bhopal"]
duplicate=[]
for ele in list1:
    if list1.count(ele)>1 and ele not in duplicate:
        duplicate.append(ele)

print(duplicate)


