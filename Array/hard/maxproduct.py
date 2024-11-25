l=[1,2,3,-1,3]
minproduct=l[0]
maxproduct=l[0]
res=l[0]
for i in range(1,len(l)):
    if l[i]<0:
        minproduct,maxproduct=maxproduct,minproduct
    maxproduct=max(l[i],maxproduct*l[i])
    minproduct=min(l[i],minproduct*l[i])
    res=max(res,maxproduct)
print(res)