l=[1,0,2,0,3,0,4,0]
k=0
for i in range(len(l)):
    if l[i]!=0:
        l[k]=l[i]
        k+=1
for i in range(k,len(l)):
    l[i]=0
print(l)
print(k)