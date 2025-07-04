'''
st="zepto"
k=3
new_str=''
for i in st:
    if ord(i) >=122-k:
        n=ord('a')-1+((ord(i)+k)%122)
        new_str+=chr(n)
    else:
        new_str+=chr(ord(i)+k)
print(new_str)
'''
ch='Zepto'
k=5
new_ch=''
for i in ch:
    new_ch+=chr(((ord(i)-ord('A')+k)%26+ord('A')))
print(new_ch)