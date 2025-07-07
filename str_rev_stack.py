s="jomon"
rev_s=''
stack=[]
for ch in s:
    stack.append(ch)
while stack:
    rev_s+=stack.pop()
print(rev_s)