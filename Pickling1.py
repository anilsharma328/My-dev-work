import pickle

"python object "
my_list=["A",1,2,3,4,5.3]
str="ABCDEF"

byte_data=pickle.dumps(my_list)
#byte_data=pickle.dumps(str)
print("pickeled data ", byte_data)

unpickled_data=pickle.loads(byte_data)
print("Unpickeled data ", unpickled_data)
