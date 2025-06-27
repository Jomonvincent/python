grades={'zyan':'A','Unni':'S','Arun':'B+','Manu':'C'}
aKeyGrades=dict(sorted(grades.items()))
dKeyGrades=dict(sorted(grades.items(),reverse=True))
print(aKeyGrades)
print(dKeyGrades)
aValueGrade=dict(sorted(grades.items(),key=lambda items:items[1]))
dValueGrade=dict(sorted(grades.items(),key=lambda items:items[1],reverse=True))
print(aValueGrade)
print(dValueGrade)
