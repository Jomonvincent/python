str="programming"
new_str=[]
rev_str=''
for i in str:
    if i not in new_str:
        new_str.append(i)
print("".join(new_str))

for i in range(len(str)-1,-1,-1):
    rev_str+=str[i]
print(rev_str)
