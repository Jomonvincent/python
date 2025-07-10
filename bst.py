class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,data,root):
        if root is None:
            return node(data)
        elif root.val>data :
            root.left=self.insert(data,root)
        elif root.val<data:
            root.right=self.insert(data,root)
        return root
    def traverse(self,root):
        if root is None:
            return 0
        else:
            print(root.val,end=" ")
            self.traverse(root.left)
            self.traverse(root.right)
t=bst()
root=None
values=[23,34,345,45,4,4,5,54]
for i in values:
    
    t.insert(i,root)

t.traverse()

