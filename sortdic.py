grades={'zyan':'A','Unni':'S','Arun':'B+','Manu':'C'}
aKeyGrades=dict(sorted(grades.items()))
dKeyGrades=dict(sorted(grades.items(),reverse=True))
print("sorted by key(asc)",aKeyGrades)
print("sorted by key(desc)",dKeyGrades)
aValueGrade=dict(sorted(grades.items(),key=lambda items:items[1]))
dValueGrade=dict(sorted(grades.items(),key=lambda items:items[1],reverse=True))
print("sorted by value(asc)",aValueGrade)
print("sorted by value(desc)",dValueGrade)
