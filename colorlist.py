colorList1=['red','green','black','white','brown','blue']
colorList2=['yellow','gold','green','cyan']
print(colorList1)
print(colorList2)
print(f"colors in colorList1 that are not in colorList2 = {set(colorList1).difference(set(colorList2))}")