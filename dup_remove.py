arr=[1,2,2,3,4,4,5]
new_arr=[]
for i in range(len(arr)):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])
print(new_arr)