text='jomon#vin##cent##'
count=0
op1=[]

for n in text:
    if n!='#':
        op1.append(n)
    else:
        count+=1
name=''.join(op1)
print(name)
print('#'*count+name)
print(name+'#'*count)

#or

print()
s=text.count('#')
n=text.replace('#','')
print(n)
print('#'*s+n)
print(n+'#'*s)