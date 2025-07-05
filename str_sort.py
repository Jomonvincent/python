st="abcaabcijaabcd"
s=list(st)
for i in range(len(s)):
    for j in range(len(s)):
        if ord(s[i])<ord(s[j]):
            s[j],s[i]=s[i],s[j]
sort_s="".join(s)
print(sort_s)
new_str=''
for i in sort_s:
    if  i not in new_str:
        new_str+=i
    else:
        continue
print(new_str)
#or do the same using dictionary
str_dic={}
for i in sort_s:
    str_dic[i]=str_dic.get(i)
for i in str_dic:
    print(i,end="")

