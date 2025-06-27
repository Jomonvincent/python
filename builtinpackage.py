import math,random,re,string,datetime
def gen_password(length):
    char=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(char) for c in range(length))
    return password
length=int(input("Enter the length of the password: "))
print(f"generated passeword: {gen_password(length)}")