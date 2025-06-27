l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
area=lambda a,b:a*b
print(f"area of a rectangle with length-{l} and breadth-{b}: {area(l,b)}")
a=int(input("Enter the kength of the square: "))
area=lambda a:a*a
print(f"area of a square with length-{a}: {area(a)}")
b=int(input("Enter the breadth: "))
h=int(input("Enter the height: "))
area=lambda b,h:(1/2)*b*h
print(f"area of the triangle with dimesions {b},{h} : {area(b,h)}")
      

