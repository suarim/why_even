import math 
n=2
m=69
for i in range(1,m+1):
    if i**n==m:
        print(i)
        break

ans=-1
low=1
high=m
while low<=high:
    mid=(low+high)//2
    if mid**n==m:
        ans=mid
        break
    elif mid**n<m:
        low=mid+1
    else:
        high=mid-1
print(ans)