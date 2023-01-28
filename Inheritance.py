
class computer:
    def __init__(self):
        self.ram ="8gb"
        self.processor= "p4"
        self.keyboard="english"

class mac(computer):
    def __init__(self):
        super().__init__()
        self.os="macos"
        self.price="1lakh"

pc1=mac()
print(pc1.__dict__)