l=[2,96,69,77,145,250]
max1=0
max2=0
index1=0
index2=0
for i in range(len(l)):
    if max1<l[i]:
        max2=max1
        max1=l[i]
        index2=index1
        index1=i
    elif max2<l[i]:
       max2<l[i]
       max2=l[i]
       index2=i

print(f"Max Element= {max2} & it is found at {index2} index")