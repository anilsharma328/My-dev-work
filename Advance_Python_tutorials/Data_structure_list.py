
# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

print("Start of Program")
expenses =[ {
    "Jan" :2200,
    "Feb" : 2350,
    "March" :2600,
    "April" : 2130,
    "May" : 2190
}
            ]

print("feb  vs Jan is : " ,expenses[0]["Feb"] -expenses[0]["Jan"])

print("Total Quarter exenses: " ,expenses[0]["Feb"] + expenses[0]["Jan"] +expenses[0]["March"])

for item,value in  expenses[0].items():
    if value ==2000 :
        print(item,value)
expenses[0]["June"] =1980
expenses[0]["April"] =expenses[0]["April"] - 200
print(expenses[0])

"""""   SUperHero Program"""
heros=['spider man','thor','hulk','iron man','Captain america']
print("length of heros array",len(heros))
heros.append("black panther")
heros.remove("black panther")
heros.insert(3,"Black panther")
heros[1:3]=["Doctor Strange"]
heros.sort()
print(heros)

'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

number=int(input("enter number"))
odd_numbers=[]
even_numbers=[]
for i in range(1,number):
    if i%2 == 1:
        odd_numbers.append(i)
    else:
        even_numbers.append(i)
print("Odd numbers",odd_numbers)
print("Even numbers",even_numbers)


