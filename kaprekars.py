#program to find numbers that dosen't lead to kaprekars numbers and to check if a specific number lead to kaprekars constant
def kap(num):
    digit=[]
    while num>0:
        digit.append(num%10)
        num=num//10
    while len(digit)<4:
        digit.append(0)
    a_num=int("".join(str(d)for d in sorted(digit)))
    d_num=int("".join(str(d)for d in sorted(digit,reverse=True)))
    if a_num>d_num:
        k=a_num-d_num
        print(a_num,"-",d_num," : ",k)
    else:
        k=d_num-a_num
        print(d_num,"-",a_num," : ",k)
    if k==6174 or k==0:
        return k
    return kap(k)

#prints numbers that doesn't lead to kaprekars constant(6174)
none_kap=[]
for num in range(1000,10000):
    k=kap(num)
    if(k==0):
        none_kap.append(num)
print(none_kap)

#check if a specific number lead to kaprekars constant
num=int(input("Enter a four digit number : "))
if num>=1000 and num<10000:
    k=kap(num)
    print(k)
    if k==6174:
        print(num," can reach kaprekar's constant")
    else:
        print(num," can not reach kaprekar's constant")

