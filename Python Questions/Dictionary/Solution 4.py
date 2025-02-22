a={1:10,2:20,3:30} 
b={3:40,4:50,5:60}
for i in b.keys():
    if i in a.keys():
        a[i]=a[i]+b[i]
    else:
        a[i]=b[i]
print(a)