class school:
   # school_name_cls = "ABC"
    def __init__(self, school_nm):
        self.school_name = school_nm
    def display_school_details(self):
        print(f" School name is : {self.school_name}")

class student(school):
    def __init__(self,student_marks,student_name):
        self.marks=student_marks
        self.name=student_name

    def display_student_details(self):
        print(f" name is : {self.name}, marks are :  {self.marks}")


sc=school("RGTU")
s1=student(34,"Anil")
sc.display_school_details()
s1.display_school_details()
#print("school_name", s1.school_name_cls)
s1.display_student_details( )

