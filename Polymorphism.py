
class BMW:
    def __init__(self):
        self.fuel_type='Petrol'
        self.engine='superspeed'
    def show_details(self):
        print(f"car name is BMW ,  engine and fuel_type are { self.fuel_type} ,{self.engine} ")

class Maruti:
    def __init__(self):
        self.fuel_type='Deisel'
        self.engine='Low'
    def show_details(self):
        print(f"car name is BMW ,  engine and fuel_type are { self.fuel_type} ,{self.engine} ")

def car_details(obj):
    obj.show_details()


mar=Maruti()
bmw_obj=BMW()

car_details(mar)
car_details(bmw_obj)
