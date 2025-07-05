def numJewelsInStones(jewels,stones):
    j={}
    for r in stones:
        if r in jewels:
            j[r]=j.get(r,0)+1
    return sum(j.values())
jewels="aA"
stones="aAAbbbb"
numJewelsInStones(jewels,stones)