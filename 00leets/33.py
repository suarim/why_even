arr = [4,5,6,7,0,1,2]
target = 5
l=0
r=len(arr)-1
while l<r:
    m=(l+r)//2
    if arr[m]>arr[r]:
        l=m+1
    else:
        r=m
print(l)
k=l
if k==0:
    l=0
    r=len(arr)-1
if target>=arr[l] and target<=arr[-1]:
    l=k
    r=len(arr)-1
else:
    l=0
    r=k
print(l,r)
while l<=r:
    m=(l+r)//2
    if arr[m]==target:
        print("found at",m)
        break
    elif arr[m]<target:
        l=m+1
    else:
        r=m-1