#string slicing
string="1234567890"
print("interchanging first & last : ",string[-1]+string[1:-1]+string[0])
print("reversed string : "+string[-1:-len(string)-1:-1])
print("slicing with +2 iteration : "+string[1::2])
print("slicing with -2 iteration : "+string[-1::-2])