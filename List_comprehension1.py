'''List comprehension
'''
print ("List comprehension")

num_list =[1,4,5,2,5,6]
num_list2= ([num *num for num in num_list ])
num_list3= ([num *num for num in num_list if num <=2])
print(num_list2)
print(num_list3)

