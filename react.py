class rectanle:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
    def __str__(self):
        return f"rectangle({self.len,self.wid})"
    def area(self):
        return self.len*self.wid
    def perimeter(self):
        return 2*(self.len+self.wid)
    def comp(self,other):
        if(self.area()>other.area()):
            return self,self.area()
        elif(self.area()==other.area()):
            return self,self.area()
        else:
            return other, other.area()
    
rect1=rectanle(5,10)
rect2=rectanle(2,8)
print(rect1.area())
print(rect2.area())
print(rect1.perimeter())
print(rect2.perimeter())
com,comval=rect1.comp(rect2)
print(com,comval)
