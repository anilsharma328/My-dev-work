
### find last_element Key value from dictionary
##Join Method
dict1={
    'A':1,
    'B':2,
    'C' :3,
    "D":4

}
List1=list(dict1.keys())

print("Last element key is : ", List1[-1] ,"Last element Value is :", dict1[List1[-1]])

str1=":".join(List1)
print("str is",str1)

str2=":".join(dict1)  ## Joins the keys

print("str2 is",str2)

set1={"India","Pakistan","Bangladesh"}
set1_str="|".join(set1)
print(set1_str)   ### Joins the set , Wont maintain the order