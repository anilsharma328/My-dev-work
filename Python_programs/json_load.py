import json
import jsonpickle
class employee:
    def __init__(self,eno,ename,age,sal):
        self.eno=eno
        self.ename=ename
        self.age=age
        self.salary=sal

    def display(self):
        print("emp id is {},Name is {},age is {},salary is {}".format(self.eno,self.ename,self.age,self.salary))

e=employee(1001,'ABCD',23,3000)

#use jsonpickle to serilize and deserilize

json_string=jsonpickle.encode(e)
print(type(json_string))

print(json_string)

##serialize to a file 
with open("emp_hson_pickle_data.json",'w') as file:
    file.write(json_string)

##deserialize to an obj
e2=jsonpickle.decode(json_string)
    
'''
#e.display()
e_dict=e.__dict__
emp_json=json.dumps(e_dict,indent=4)
#print(emp_json)

with open("emp_data_file.json",'w') as f:
    json.dump(emp_json,f,indent=4)

with open("emp_data_file.json",'r') as f:
   e_dic=json.load(f)

print(type(e_dic))
#for i ,j in e_dic.items():
#    print(i)

#e=employee(e_dic["eno"],e_dic["ename"],e_dic["age"],e_dic["salary"])
'''
