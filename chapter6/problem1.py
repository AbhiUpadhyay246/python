a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
d = int(input("enter fourth number:"))
if(a>b and a>c and a>d):
    print(f"the greatest number is a :{a}")
elif(b>a and b>c and b>d):
    print(f"the greatest number is b :{b}")    
elif(c>a and c>b and c>d):
    print(f"the greatest number is c :{c}")    
elif(d>a and d>b and d>c):
    print(f"the greatest number is d :{d}")    
else:
    print("all number is equal")    
