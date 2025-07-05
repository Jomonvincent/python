
def uniq(message):
    mdic={}
    for ch in message:
        mdic[ch]=mdic.get(ch,0)+1
    for ch in message:
        if mdic[ch]==1:
            return ch
message='ababbcddexx'
print(uniq(message))

'''
t=[]

for i in message:
    if message.count(i)==1:
        t.append(i)
print(t[0])

'''
    