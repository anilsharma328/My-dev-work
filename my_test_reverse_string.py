#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
str="We will conquere COVID-19"
my_list=[]
for r in str:
    #print (r,sep='')
     my_list.append(r)

rev_str=''

while len(my_list) != 0:
    rev_str= rev_str + my_list.pop()
   # print(my_list)
print(rev_str)
    
