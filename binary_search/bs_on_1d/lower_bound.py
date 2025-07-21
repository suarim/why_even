arr=[1,2,3,4,6,7]
l=0
r=len(arr)-1
ans=0
while l<r:
    m=(l+r)//2
    if arr[m]<5:
        l=m+1
    else:
        ans=m
        r=m-1
else:
    print(ans)
