l=[4,2,2,6,4]
res=set()
for i in range(len(l)):
    b=l[i]
    if b==6:
        res.add(tuple([b]))
    for j in range(i+1,len(l)):
        b^=l[j]
        if b==6:
            res.add(tuple(l[i:j+1]))
print(res)
max=max([len(i) for i in res])
print(max)