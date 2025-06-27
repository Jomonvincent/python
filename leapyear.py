y1=int(input("Enter the starting year: "))
y2=int(input("Enter the last year: "))
c=0
for i in range(y1,y2+1):
    if(i%4==0 and i%100!=0) or (i%400==0):
        print(i,"is a leap year")
        c+=1
print("there are ",c,"leap years in between ",y1,"and",y2)