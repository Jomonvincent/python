#very important
def isValid(s):
    dic={'(':')', '{':'}', '[':']'}
    st=[]

    for ch in s:
        if ch in dic:
            st.append(ch)
        elif st and dic[st[-1]] == ch:
            st.pop()
        else:
            return False

    if len(st) == 0:
        return True
    else:
        return False

s="([)]"
print(isValid(s))