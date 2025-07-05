spam="hi jomon@gmail.com there ,how are you +911"
cons=["@","mail","+911"]
for i in cons:
    if i in spam:
        print("spam")
        break
print("not spam")

