import math
arr=[3,6,7,11]
k=8
def hours(arr,k):
    return (sum([math.ceil(i/k) for i in arr]))
l=0
r=max(arr)
ans=0
while l<=r:
    m=(l+r)//2
    if hours(arr,m)<=k:
        ans=m
        r=m-1
    else:
        l=m+1
print(ans)

