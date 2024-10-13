l=[3,2,2,3]
k=0
for i in range(len(l)):
    if l[i]!=3:
        l[k]=l[i]
        k+=1
print(l)
print(k)