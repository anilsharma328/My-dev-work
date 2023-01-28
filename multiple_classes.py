class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    def display(self):
        print("employee Name", self.name)
        print("employee salary",self.sal)


#######  second class   
class manager:
    def update_salary(emp):
        emp.sal =emp.sal +100
        emp.display()

emp=employee("Anil",2000)
manager.update_salary(emp)
