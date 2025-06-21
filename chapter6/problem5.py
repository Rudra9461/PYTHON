marks = int(input("enter the marks : "))
if(marks<=100 and marks>=90):
    grade = 'Ex'
if(marks<90 and marks>=80):
    grade = 'A'
if(marks<=80 and marks>=70):
    grade = 'B'
if(marks<=70 and marks>=60):
    grade = 'C'
if(marks<=60 and marks>=50):
    grade = 'D'    
if(marks<=50 and marks>=40):
    grade = 'F'    

print(grade)