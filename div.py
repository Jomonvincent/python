#1-9,10:A,11:B,12:C,......26:Z
def div(n,num):
    result=""
    while num>0:
        r=num%n
        if r>9:
            result+=chr(55+r)
        elif r<=9:
            result+=str(r)
        num=num//n
    result=result[::-1]
    return result
print(div(12,718))