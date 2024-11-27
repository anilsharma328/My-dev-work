class A:
    a=123
    def __init__(self):
        print("this is parent constructor")
        self.b=342
    def parent_method(self):
        print("this is parent method")
    @classmethod
    def parent_class_method(cls):
        print("this is parent class method")
    @staticmethod
    def parent__static_method():
        print("this is parent static method")
        
class B(A):
    def __init__(self):
        super().__init__()
        super().parent_method()
        super().parent_class_method()
        super().parent__static_method()       

    def b_child(self):
        super().__init__()
        super().parent_method()
        super().parent_class_method()
        super().parent__static_method() 
    @classmethod
    def b_child_class_method(cls):
        #super().__init__()  ## You can nnot call as these are object based things
        #super().parent_method()
        super(B,cls).__init__(cls)  ## Alternate way to call parent class method
        super(B,cls).parent_method(cls)
        super().parent_class_method()
        super().parent__static_method() 

b=B()
print("  *   " *12)
b.b_child()
print("  *   " *12)
B.b_child_class_method()
#b.m1()


