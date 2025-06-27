with open("ren.txt",'w') as ren:
    ren.write("news flash \ni wa created at the dawn of creation \ni am temptation\ni am the snake in ethan \ni am th reason for treason\nbeheading all kings\ni am sin\nwith no rhyme or reason")
with open("ren.txt",'r') as ren:
    lines=ren.readlines()
    
newline=[line.strip() for line in lines]
print(newline)

#OR
#newline=[]
#for line in lines:
#    newline.append(line.strip())
#print(newline)
         
