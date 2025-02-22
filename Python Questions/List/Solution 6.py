l=[1,2,3,4,20]
for i in range(len(l)-1):
    if l[i]<=l[i+1]:
        continue
    else:
        print("Your List is Unsorted")
        break
else:
    print("Your list is Sorted")
