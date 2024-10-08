l=[1,3,-2,-3,9]
ans=[0 for _ in range(len(l))]
k,j=1,0
for i in l:
    if i<0:
        ans[k]=i
        k+=2
    else:
        ans[j]=i
        j+=2
print(ans)