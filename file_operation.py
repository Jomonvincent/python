#file mainpulation
f1=open("secfile.txt","w")
f1.write("this is my first file in python.\n wanto work with files\nthis is my third line")
f1=open("secfile.txt","r")
ff=f1.readlines()
print(ff)



