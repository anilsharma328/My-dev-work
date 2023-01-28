class emp:
    def __init__(self,name,age,city,department):
        self.name=name
        self.age=age
        self.city=city
        self.department=department

    def display_emp_info(self):
        print("Name is : {},\nAge is : {},\nCity is : {},\nDepartment is : {}".format(self.name, self.age, self.city,self.department))

class emp_audit(emp):
    def __init__(self,name,age,city,department,emp_id,bonus):
        super().__init__(name,age,city,department)  ###provide properties to parent class
        self.emp_id=emp_id
        self.bonus=bonus

    def display_emp_info(self):
        super().display_emp_info()  ## call parent method 
        print("Employee Id is : {}\nBonus is :{}".format(self.emp_id, self.bonus))

emp_aud=emp_audit('Anil',33,'Bhopal','IT',11167538,30000)
emp_aud.display_emp_info()
