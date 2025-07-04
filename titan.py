d=200
m=5
ad=[10,20,30,20,10]
rt=[1,2,5,2,1]
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


    

        






        

        
