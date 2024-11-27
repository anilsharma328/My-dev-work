## "Watermelon,5|carrot,30|apple,10|baNANA,10|orange,15|bean,70|potato,30"
### store
class Store:
    def __init__(self):
        pass
    #def Show_fruits:
  #      pass

veg="Watermelon,5|carrot,30|apple,10|baNANA,10|orange,15|bean,70|potato,30"
fruit_list=veg.split("|")
fruit_dict={}
for fruits_name in fruit_list:
    fruit_key,val= fruits_name.split(",")
    #print(fruit_key,val)
    fruit_dict[fruit_key] =val
print(fruit_dict)

str=Store()

# "Watermelon,5|carrot,30|apple,10|baNANA,10|orange,15|bean,70|potato,30"

def update_count(fruit_dict, fruit_name, count ):

    if int(fruit_dict[fruit_name]) < count:
        if  fruit_name in fruit_dict:
           if int(fruit_dict[fruit_name]) + count > 0:
             fruit_dict[fruit_name] = int(fruit_dict[fruit_name]) + count
           else :
             print(" Stock not available", fruit_name, end=" ")
        else :
          fruit_dict[fruit_name] = count
    else :
        print(" Stock not available"  ,fruit_name, end=" ")

fruit_name=input("FruitName : " )
count= int(input("count :"))
print(fruit_dict)
update_count(fruit_dict,fruit_name,count )

