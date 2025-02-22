l=[]
r=[]
a=int(input("Enter Size of your list : "))
for i in range(a):
    val=int(input("Enter number and Press Enter : "))
    l.append(val)
for i in range(len(l)-1,-1,-1):
    r.append(l[i])
print("Original List : ",l)
print("Reversed list : ",r)