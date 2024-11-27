print("start of Program")

class Node:
    def __init__(self,data):
        self.data=data;
        self.reference=None;
node1=Node(7)
print("data is" ,node1.data)
print("Reference is ", node1.reference)