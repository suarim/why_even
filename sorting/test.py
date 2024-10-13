l=[8,7,6,5,4,3,2,1]
for i in range(len(l)):
    for j in range(i,0,-1):
        if l[j]<l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]
        else:
            break
print(l)