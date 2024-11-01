#WAP To check Whether a given number is Armstrong or not.
i=int(input("Enter number to check for Armstrong:"))
orig=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("Number is Armstrong")
else:
    print("Number is Not Armstrong")
#Armstrong means Number ^ no of digits.
#Ex- No= 153   1^3+5^3+3^3=153(Armstrong)