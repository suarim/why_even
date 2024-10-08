l=[1,2,3,4,5,-1]
k=0
for i in range(1,len(l)):
    if l[i]<l[i-1]:
        print("Not sorted")
        k=1
        break
if k==1:
    pass
else:
    print("Sorted")