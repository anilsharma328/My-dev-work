my_str="my name is anil Sharma "
my_list=my_str.split()
list1=[]
for i in range(len(my_list)):
    list1.append((my_list[i][  : :-1 ]))
    #pass

print(my_str)
print(list1)
my_reverse_str=" ".join(list1)
print(my_reverse_str)

