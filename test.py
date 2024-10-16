import math
arr=[30,11,23,4,20]
k=5
def helper(arr,m):
    return sum([math.ceil(i/m) for i in arr])
l=0
ans=float('inf')
r=max(arr)
while l<=r:
    m=(l+r)//2
    if helper(arr,m)<=k:
        ans=m
        r=m-1
    else:
        l=m+1
print(ans)