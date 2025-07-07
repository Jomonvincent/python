s="baaab"
t="abba"
def com(s):
    stack=['o']
    for ch in s:
        if ch!=stack[-1]:
            stack.append(ch)
        else:
            stack.pop()
    return stack
print("".join(com(s))[1:])
print("".join(com(t))[1:])
