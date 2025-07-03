#program to get extension to a file
ex=input("Enter the file name: ")
if '.' in ex:
    ex=ex.split('.')
    print(f"extension = {ex[-1]}")
else:
    print("Invalid file name")
