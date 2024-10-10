arr=[3,5,8,9,15,19]
l=0
r=len(arr)-1
ans=0
while l<r:
    m=(l+r)//2
    if arr[m]<=9:
        l=m+1
    else:
        ans=m
        r=m-1
print(m)
