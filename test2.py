
class student():
   def __init__(self,name,age,maths,hindi):
      self.name=name
      self.age=age
      self.student_marks=self.marks(maths,hindi)

   def display_dtl(self):
      print("Hello ",self.name, "your age is :",self.age)

   class marks():
      def __init__(self,maths,hindi):
         self.maths=maths
         self.hindi =hindi

      def display_marks(self):
         print("Maths Marks : ", self.maths, "\nHindi Marks :", self.hindi)


s1= student('anil',24,50,34)

s2=student.marks(60,75)
s1.display_dtl()
s2.display_marks()
#print ( s1.student_marks.maths )
s1.student_marks.display_marks()

print("hi")
