n=int(input("Enter a number to chek Prime or composite :"))
count=0
for i in range(1,n+14):
    if n%i==0:
        count=count+1
if count<=2:
    print(n," is a Prime number")
else:
    print(n, "is  a composite number")