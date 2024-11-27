from enum import Enum

class Test(Enum):
    studentname="Anil"
    rollNumber= 7
    Branch="IT"
    percentage=67.5

class subject(Enum):
        subject_name="Maths"
        Teacher="JhingurLal"

#print(Test.studentname.name)

for student in Test:
    #print(Test.studentname.value)
    print(f"members of Student Class are: {student.name}: {student.value}")

#print(f"Name of Student: {Test.studentname.value} and his subject is {subject.subject_name.value} and Teacher is {subject.Teacher.value}")
#print(f"Roll Number is : {Test.rollNumber.value}")
#print(f"Department: {Test.Branch.value}")
#print(f"Percentage are: {Test.percentage.value}")
