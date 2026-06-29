mark = int(input("enter the marks :"))

if(mark<=100 and mark>=90):
    grade="Ex"
elif(mark<90 and mark>=80):
    grade="A"
elif(mark<80 and mark>=70):
    grade="b"
elif(mark<70 and mark>=60):
    grade="c"
elif(mark<600 and mark>=50):
    grade="d"
elif(mark<50 ):
    grade="f"
print("your grade is:",grade)
