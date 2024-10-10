arr=[4,5,6,7,0,1,2]
l=0
r=len(arr)-1
while l<r:
    m=(l+r)//2
    if arr[m]>arr[r]:
        l=m+1
    else:
        r=m
print(l)