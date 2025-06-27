list1=[23,54,73,89]
list2=[89,55,12]
#length
if(len(list1)==len(list2)):
    print("both list are of the same length : ",+len(list1))
else:
    print("both list are of different length")

#sum
if(sum(list1)==sum(list2)):
    print("both list are of the same sum : ",+sum(list1))
else:
    print(f"both list have different sum list1: {sum(list1) }, list2:{sum(list2)}")

#value in both
    both=set(list1).intersection(set(list2))

    if(both):
        print(f"both list have common values: {both}")
    else:
        print("both list have no common values")
        
