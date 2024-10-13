l=[1,1,1,1,2,2,2,3,3,4,4,5]
k=1
for i in range(1,len(l)):
    if l[i]!=l[i-1]:
        l[k]=l[i]
        k+=1
print(l)