n=10

for i in range(1,n+1,2):
    print(("*"*i).center(n,' ')+" "*n+("*"*i).center(n,' '))
for i in range(n):
    print('*'*n+' '*n+"*"*n)
for i in range(n//2):
    print("*"*n*3)
for i in range(n):
    print("*"*n+" "*n+"*"*n)
    