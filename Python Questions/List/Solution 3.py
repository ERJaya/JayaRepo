l=[12,87,54,97,-34,13]
pos=[]
neg=[]
for i in range(0,len(l),1):
    if l[i]>0:
        pos.append(l[i])
    else:
        neg.append(l[i])
print("Given list: ",l)
print(f"Positive Elements : {pos} & Negative Elements : {neg}")