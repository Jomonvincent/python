class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current:
            current=current.next
        current.next=new_node
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")

n=0
ll=linkedList()
while n<5:
    a=int(input("Enter a value  : "))
    ll.insertAtEnd(a)
    n+=1
ll.display()
    