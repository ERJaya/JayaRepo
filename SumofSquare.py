#Program to find sum of square  from 1 to n.
n=int(input("Enter no upto which you want to sum:"));
i=1
sum=0
while(i<=n):
    sum=sum+(i*i)
    i=i+1
print("Sum=",sum);