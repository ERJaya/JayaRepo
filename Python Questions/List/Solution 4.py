l=[2,96,69,77,145,20]
max=0
pos=0
for i in range(len(l)):
    if l[i]>max:
     max=l[i]
     pos=i
print(f"Max Element= {max} & it is found at {pos} index")