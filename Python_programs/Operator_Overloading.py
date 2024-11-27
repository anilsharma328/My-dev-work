class Test:
    def __init__(self,num):
        self.num=num
    def __gt__(self, other):
        if self.num > other.num:
            return "Bada hai"
        else:
            return "chota hai"

    def __add__(self, other):
        return "ja nahi karna add"

T1=Test(1000)
T2=Test(200)

print(T1 > T2)
print(T1 + T2)