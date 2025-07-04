string="Adi1Shankara2College"
string=string.lower()
def countVC(string):
    v_count=0
    c_count=0
    vowels=['a','e','i','o','u']
    numbers=['1','2','3','4','5','6']
    for ch in string:
        if ch in vowels:
            v_count+=1
        elif ch not in vowels:
            if ch not in numbers:
                c_count+=1
    return v_count,c_count

print(string)
print(countVC(string))
print(len(string))