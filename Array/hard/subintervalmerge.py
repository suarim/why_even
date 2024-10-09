l=[[1,2],[2,6],[8,10],[9,17],[15,18]]
res=[l[0]]
for i,j in l[1:]:
    last=res[-1][1]
    if last>=i:
        res[-1][1]=max(j,res[-1][1])
    else:
        res.append([i,j])
print(res)