
string1="ABCDEF"

result=""
print("Original String")
for i in string1:
    result=i + result
print("New  String")
print(result)
print("2nd   String")
print(string1[::-1])