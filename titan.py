d=300
m=5
ad=[10,20,30,10,20]
rt=[1,2,3,1,2]
na=[0]*len(ad)
tc=0
while d>0:
    cd=0
    i=0
    while(i<m):
        if tc>=na[i]:
            na[i]=rt[i]
            cd+=ad[i]
        i+=1
    d-=cd
    tc+=1
print(tc)

#or we can read input as
d,m=map(int,input("Enter damage and no. of squads").split())
ad=list(map(int,input().split()))
rt=list(map(int,input().split()))

    

        






        

        
