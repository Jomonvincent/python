#we need to find the number of iteration it will take to kill the titan
d=200           #health of the titan
m=5             #no of squads
ad=[10,20,30,20,10] #damage of every squad
rt=[1,2,5,2,1]
na=[0]*len(ad)
tc=0
while d>0:
    cd=0
    i=0
    while(i<m):
        if tc>=na[i]:
            cd+=ad[i]
            na[i]+=rt[i]
        i+=1
    tc+=1
    d-=cd
print(tc) 


    
