class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    def compare(self,other):
        if self.area()>other.area():
            return f"{self} is larger"
        elif self.area()<other.area():
            return f"{other} is larger"
        else:
            return f"{self} and {other} have the same area"
    def __str__(self):
        return f"Rectanle(length: {self.length} ,width: {self.width})"

rect1=rectangle(5,10)
rect2=rectangle(7,5)
print(rect1)
print(rect2)
print(f"Area of rect1= {rect1.area()}")
print(f"Area of rect2= {rect2.area()}")
print(f"Permieter of rect 1= {rect1.perimeter()}")
print(f"Permieter of rect 2= {rect2.perimeter()}")
print(f"{rect1.compare(rect2)}")