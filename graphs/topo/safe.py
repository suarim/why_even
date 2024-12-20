l = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
k=[]
res=[]
for i,n in enumerate(l):
    if len(n)==0:
        k.append(i)
        res.append(i)

for i in range(len(l)):
    for j in range(len(l[i])):
        if len(l[i])==1 and l[i][0] in k:
            res.append(i)
print(sorted(res))