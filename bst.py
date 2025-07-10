class node:
    def __init___(self,val):
        self.val=val
        self.left=None
        self.right=None
class bst:
    def __init(self):
        self.root=None
    def insert(self,root,data):
        if root is None:
            root=node(data)
        elif root.val>data:
            root.left=node(data)
        elif root.val<data:
            root.right=node(data)
    def traverse(self,root):
        if root is None:
            return 0
        else:
            print(root.val,end="-->")
            self.traverse(root.left)
            self.traverse(root.right)
t=bst()
for i in range(10):
    t.insert(int(input("Enter the node value : ")))
t.traverse()

