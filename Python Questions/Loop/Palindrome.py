n=int(input("Enter a number :"))
copy=n
rev=0
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
if copy==rev:
    print(copy," is a Palindrome number")
else:
    print(copy," is not a palindrome number")