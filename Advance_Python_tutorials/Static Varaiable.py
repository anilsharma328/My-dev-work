''''Static Varaiable '''
class Test:
    familyname='Sharma'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Test.city='BHOPAL'
        print('inside constuctor using self',self.familyname)
        print('inside constuctor using classname ',Test.familyname)
    def show_details(self):
        print('inside instance class self',self.familyname)
        print('inside instance class using classname ',Test.familyname)
        print("emp name is ",self.name+ ' '+self.familyname,"age is ",self.age)
    @classmethod
    def status(cls):
        Test.marriage_status='Married'
        print('inside class method using cls',cls.familyname)
        print('inside class method using Classname ',Test.familyname)

    @staticmethod
    def education():
        Test.education_status='BE'
        print('inside static method using Classname ',Test.familyname)


t=Test('Anil',33)
t.show_details()
print(t.__dict__)
t.status()
t.education()

t2=Test('Shikha',32)
t2.show_details()
print('Ouside class using Classname ',Test.familyname)
print('Ouside class using obj ',t.familyname)
#print(t2.__dict__)  ###  Instance variables 
#print(Test.__dict__['familyname']) ##  Class level variable 
#print(Test.__dict__['city']) 
#print(Test.__dict__) 
