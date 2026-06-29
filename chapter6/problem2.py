mark1 = int(input("enter the number :"))
mark2 = int(input("enter the number :"))
mark3 = int(input("enter the number :"))
total_percentage =(100*(mark1+mark2+mark3))/300
if(total_percentage>=40 and mark1>33 and mark2>33 and mark3>33):
    print("you are passed:",total_percentage)
else:
    print("you failed , try again next year:",total_percentage)
