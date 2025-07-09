def pat(n):
    for i in range(1,n,2):
        print((i*".|.").center(n*3,'-'))
    print("WELCOME".center(n*3,'-'))
    for i in range(n-2,-1,-2):
        print((i*".|.").center(n*3,'-'))

n,m=map(int,input().split())
pat(n) 
#for n=7
#---------.|.---------
#------.|..|..|.------
#---.|..|..|..|..|.---
#-------WELCOME-------
#---.|..|..|..|..|.---
#------.|..|..|.------
#---------.|.---------