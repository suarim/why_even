l=[0,0,0,0,1,-2,2,4,-4]
res=set()
for i in range(len(l)):
    b=l[i]
    if b==0:
        res.add(tuple([b]))
    for j in range(i+1,len(l)):
        b+=l[j]
        if b==0:
            res.add(tuple(l[i:j+1]))
print(res)
max=max([len(i) for i in res])
print(max)