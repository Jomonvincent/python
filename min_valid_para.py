s='((())))'
dic={}
for ch in s:
    dic[ch]=dic.get(ch,0)+1
print(dic)
if int(dic['('])>int(dic[')']):
    print(int(dic['('])-int(dic[')']))
elif int(dic['('])<int(dic[')']):
    print(int(dic[')'])-int(dic['(']))