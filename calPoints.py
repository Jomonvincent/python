def calPoints( operations):
    ops=[]
    for ch in operations:
        if ch=='C':
            ops.pop()
        elif ch=='+':
            ops.append(int(ops[-1])+int(ops[-2]))
        elif ch=='D':
            ops.append(2*int(ops[-1]))
        else:
            ops.append(int(ch))
    return sum(ops)
operations = ["5","2","C","D","+"]
calPoints(operations)