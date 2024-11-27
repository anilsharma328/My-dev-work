
class computer:
    def __init__(self):
        self.__ram ="8gb"
    def display_details(self):
        print(f"RAM is {self.__ram}")

c1=computer()
c1.display_details()

class super_computer():
    def __init__(self):
        c1.__ram="16GB"

s1=super_computer()
print(c1.__dict__)
