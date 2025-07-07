class Stack:
    def __init__(self):
        self.s=[]
    def push(self, item):
        self.s.append(item)
    def pop(self):
        if not self.s:
            print("Stack empty")
        else:
            return self.s.pop()
    def peek(self):
        print(self.s[-1])
    def isEmpty(self):
        if len(self.s)==0:
            print("stack is empty")
        else:
            print("stack is not empty")

s1=Stack()
print(s1.isEmpty())
for i in range(4):
    item=int(input(f"Enter the {i}th item : "))
    s1.push(item)
print(s1.s)
print(s1.pop())
print(s1.isEmpty())



