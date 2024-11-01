#Program to check Greatest Number among 3
a=int(input("Enter 1st number"));
b=int(input("Enter 2nd number"));
c=int(input("Enter 3rd number"));
if a>b and a>c:
    print("Max no=",a);
elif b>c and b>c:
    print("Max no=",b);
else:
    print("Max no=",c);