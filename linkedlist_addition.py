class linkednode:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add(self,data):
        new_node=linkednode(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def preorder(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
l1=linkedlist()
l2=linkedlist()

for i in range(5):
    l1.add(int(input("Enter the value for l1 : ")))

for i in range(3):
    l2.add(int(input("Enter the value for l2 : ")))
print("l1 : ",end=" ")
l1.preorder()
print("l2 : ",end=" ")
l2.preorder()
    
