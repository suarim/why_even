l=[5,10,-15,0,7,8,9,-10,19,20]
prefixmap={0:-1}
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
prefixsum=0
res=0
for i,n in enumerate(l):
    prefixsum+=n
    if prefixsum in prefixmap:
        res=max(res,i-prefixmap[prefixsum])
    else:
        prefixmap[prefixsum]=i
print(res)