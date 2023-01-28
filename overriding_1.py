class parent:
    def property():
        print("I have 1 car")

    def welcome(self):
        print(" Welcome to single parking house ")


class child(parent):
    def welcome(self):
        super().welcome()
        print(" I want extra space to park my scooter")


c=child()
c.welcome()
        
