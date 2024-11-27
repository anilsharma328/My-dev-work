class engine:
    def __init__(self):
        pass
    def engine_prod(self):
        print("this is engine class")
        self.power="125kw"

    
        
class car:
    def __init__(self):
        print("this is car Object")
        self.engine_obj=engine()
        self.engine_obj.engine_prod()
        print("engine power is ",self.engine_obj.power)

c1=car()
