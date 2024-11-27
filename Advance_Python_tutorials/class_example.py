
class Test():
    def __init__(self,name,age):
      self.student_nm= name
      self.student_age=age

    def display_details(self):
        print(f"name is {self.student_nm} ,age is {self.student_age}")

s1=Test('Anil',34)
s1.display_details()

print(s1.__dict__)

print(getattr(s1,'student_age'))
setattr(s1,'student_nm','subhash')
print(getattr(s1,'student_nm'))

delattr(s1,'student_age')
#delattr(s1,'student_nm')
print(s1.__dict__)
print(hasattr(s1,'student_nm'))
#s1.display_details()