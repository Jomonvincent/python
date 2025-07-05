
def ulog(mge):
    dic={}
    for i in mge:
        dic[i]=dic.get(i,0)+1
    print(dic)
    for i in dic:
        print(i+str(dic[i]),end="")
mge="aaaabbbcc"
ulog(mge)