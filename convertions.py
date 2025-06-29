#converting a list to int with join
digit=[3,4,6,6,5]
print(digit)
num=int("".join(str(d) for d in digit))
print(num)
'''

#converting list to int without using join
digit=[3,4,6,6,5]
print(digit)
num=0
for d in digit:
    num=num*10+d
print(num)

#wrong convertion of list to str
digit=[34,45,66,67,52]
string=str(digit)               #[34,45,66,67,52] this becomes actual string 
print(string,"hi there")

'''  