### Created a class Node with two instance variables 
class Node:  
    def __init__(self,data):
        self.data = data
        self.ref = None

## created a class Linkedlist, head is intialized with None 
class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            #n = self.head
            while self.head is not None:
                print(self.head.data,'==>',end ='')
                self.head = self.head.ref

    def add_begin(self,data):
        new_node = Node(data)     ## Object of Node class 
        new_node.ref = self.head  ## set address to head 
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("node is not presesnt in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


LL1=LinkedList() ## Object of LinkedList class

LL1.add_begin(10) #Add 1st element
LL1.add_end(120)
LL1.add_begin(20) #Add 1st element
LL1.add_after(200,10)

LL1.print_LL()
