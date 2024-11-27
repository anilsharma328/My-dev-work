
class Dog():
     def __init__(self,breed,name):
        self.breed=breed
        self.name=name

     def bark(self):
        print("wao wao.name is {}".format(self.name))

    # bark("lebradog")
my_dog=Dog('lab','Lebra')
my_dog.bark()