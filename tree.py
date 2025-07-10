class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
'''        
class Tree:
    def __init__(self):
        root=None
    def insert(self,data):
        if self.root is None:
            root=node(data)
        elif root.left==None:
            root.left=node(data)
        else:
            root.right=node(data)
'''
def preorder(root):
    if not root:
        return 0
    else:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
def inorder(root):
    if not root:
        return 0
    else:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def postorder(root):
    if not root:
        return 0
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

def cnode(root):
    if root is None:
        return 0    
    else:
        return 1+cnode(root.left)+cnode(root.right)
    
def nodesum(root):
    if root is None:
        return 0
    else:
        return root.data+nodesum(root.left)+nodesum(root.right)

def tree_height(root):
    if root is None:
        return 0
    else:
        hleft=tree_height(root.left)
        hright=tree_height(root.right)
        return max(hleft,hright)+1
def depth(root,n,d=0):
    if root is None:
        return -1
    else:
        if root.data==n:
            return d
        left=depth(root.left,n,d+1)
        if left!=-1:
            return left
        return depth(root.right,n,d+1)
            
        

        
root=node(10)
root.left=node(20)
root.right=node(90)
root.left.left=node(30)
root.left.right=node(80)
root.left.left.left=node(40)
root.left.left.right=node(50)
root.left.right.left=node(60)
root.left.right.right=node(70)
root.right.right=node(100)
root.right.right.left=node(110)
root.right.right.right=node(120)
root.right.right.right.left=node(140)
root.right.right.right.right=node(150)


preorder(root)
print("\n")
postorder(root)
print("\n")
inorder(root)
print("\n")
print(cnode(root))
print(nodesum(root))
print(tree_height(root))
print(depth(root,110))