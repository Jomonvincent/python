def isPower(num):
    if num%2!=0:
        return -1
    else:
        count=0
        while num>=1:
            count+=1
            if num%2==0:
                num=num/2
            else:
                return -1
        return count
print(isPower(1))