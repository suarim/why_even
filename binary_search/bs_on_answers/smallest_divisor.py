import math
arr=[1,2,5,9]
t=7
low=1
ans=-1
high=max(arr)
while low<=high:
    mid=(low+high)//2
    if sum([math.ceil(i/mid) for i in arr])<=t:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)