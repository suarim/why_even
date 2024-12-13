arr=[3,3,3,1,2,1,1,2,2,3,3,4]
l=0
maxs=0
d={}
for i in range(len(arr)):
    fruit=arr[i]
    if fruit not in d:
        d[fruit]=1
    else:
        d[fruit]+=1
    while len(d)>2:
        d[arr[l]]-=1
        if d[arr[l]]==0:
            del d[arr[l]]
        l+=1
    maxs=max(maxs,i-l+1)
print(maxs)
    