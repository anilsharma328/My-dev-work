
import json
'''
employee= {
    "Name":"Anil",
    "Age":33 ,
    "college":"SDBCT" ,
    "Salary":None,
    "married":True
    }
employee_json=json.dumps(employee,indent=2,sort_keys=True)
print (employee)
print(type(employee))


with open('emp.json', 'w') as file:
    json.dump(employee,file)
    
'''

with open('emp.json', 'r') as file:
    employee_data=json.load(file)

print(type(employee_data))
print(employee_data)
for key,value in employee_data.items():
    print("Key is :",key,"==> Value is :",value)
