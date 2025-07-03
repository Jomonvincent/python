sp=[7,1,5,6,4,7,8,9]
min=sp[0]
max=0
for s in sp:
    if s<min:
        min=s
    elif s-min>max:
        max=s-min
print(max)
    
  