l=[2,3,15,15,3,2]
b=[]
for i in range(len(l)-1,-1,-1):
    b.append(l[i])
print(b)
if l==b:
    print("The list is Palindrome")
else:
    print("The List is not Palindrome")