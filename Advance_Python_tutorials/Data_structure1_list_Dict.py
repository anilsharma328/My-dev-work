
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