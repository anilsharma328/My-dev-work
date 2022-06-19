'''  Multi Level Inheritance     ''''
class Grandparent():
    def net_asset_val(self):
        return 200

class father(Grandparent):
    def net_asset_val(self):
        return 100

class child(father):
    def salary(self):
        return 50

gp=Grandparent()
dad=father()
son=child()

print(gp.net_asset_val())

print(son.net_asset_val()) ###  Son dont have net_asset_val but he will pull these details
# from father although his grant parent has this function. 
print(gp.net_asset_val())
