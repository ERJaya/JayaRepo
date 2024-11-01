#program to find sum of cube of digits of a given number.
i=int(input("Enter no to find sum of cube of digits:"));
sum=0
while(i>0):
    Sum=sum+(i*10)*(i*10)*(i*10)
    i=i//10
print("Sum of cube of each digits=",Sum);