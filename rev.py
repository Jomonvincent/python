#Reversing a string without changing the special characters
st="s$tu-de&n*t"
str=[]
for i in st:
    str.append(i)
print(st)

i=0
j=len(str)-1
while i<j:
    if str[i].isalpha() and str[j].isalpha():
        str[i],str[j]=str[j],str[i]
        i+=1
        j-=1
    elif str[i].isalpha():
        j-=1
    elif str[j].isalpha():
        i+=1
    else:
        i+=1
        j-=1
print("".join(str))

