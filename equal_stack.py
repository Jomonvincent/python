def equalStacks(h1, h2, h3):
    s1=sum(h1)
    s2=sum(h2)
    s3=sum(h3)
    if s1==0 or s2==0 or s3==0:
        return 0
    while True:
        if s1==s2==s3:
            return s1
        elif s1>=s2 and s1>=s3:
            s1-=h1.pop()
            print("s1",s1)
        elif s2>=s1 and s2>=s3:
            s2-=h2.pop()
            print("s2",s2)
        else:
            s3-=h3.pop()
            print("s3",s3) 

h1=[3,2,1,1,1]
h2=[4,3,2]
h3=[1,1,4,1]
print(equalStacks(h1,h2,h3))