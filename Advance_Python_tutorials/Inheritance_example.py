class product():
    def __init__(self,colour,price):
        print("This is parent class")
        self.colour=colour
        self.price=price


class Mobile(product):
    def __init__(self,brand):
        print("this is child class")
        self.brand=brand
       # print("first object : ",m.self.colour,"price : ",m.price)
        print("Second object : ",b.colour,"price : ",b.price)


p=product("Black",2000)
b=product("blue",3000)
m=Mobile("LG")
    
    
