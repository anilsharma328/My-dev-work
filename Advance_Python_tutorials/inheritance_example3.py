''' Multiple inheritance
the order class child(Mother,Father) decides the sequence of executaion
'''
class Father():
    def __init__(self):
        self.cast='Modi'
    def show_surname(self):
        print("Surname is ",self.cast)

class Mother():
    def __init__(self):
        self.cast='mahaModi'
    def show_surname(self):
        print("Surname is ",self.cast)
        
class child(Mother,Father):
        pass
    #def __init__(self,age):
        #super().__init__()
        #self.age=age
        #print('cast and surname are ',self.cast, self.age)

son=child()
son.show_surname()
#father=Father()
