a=[1,1,2,3,4,1,2,5,7,6,8,4,1,2,4,8,8,7]
dict={}
for i in a:
    if i in dict.keys():
     dict[i]=dict[i]+1
    else:
       dict[i]=1
print(dict)
