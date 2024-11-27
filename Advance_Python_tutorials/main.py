
string="zaxbcabdbwsb"
my_dict={}
max_word=""
max_length=0
for i in range(0,len(string)):
   if string[i] in my_dict:
    print(string[i],"is available")
    print('position',"first",my_dict[string[i]],"Next ",i)
    max_word = string[ my_dict[string[i]]:i]
    my_dict[string[i]]=i
    max_length=i - my_dict[string[i]]
   else:
    print(string[i],"is not available")
    max_length=max_length+1
    my_dict[string[i]]=i

print(my_dict)
print(max_length)
print("max_string",max_word)

