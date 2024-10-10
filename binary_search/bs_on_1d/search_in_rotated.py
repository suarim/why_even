arr=[4,5,6,7,0,1,2]
l=0
k=99
r=len(arr)-1
while l<r:
    m=(l+r)//2
    if arr[m]>arr[r]:
        l=m+1
    else:
        r=m
print(l)
t=l
l=0
r=0
if k>=arr[t] and k<=arr[-1]:
    l=t
    r=len(arr)-1
elif k>=arr[0] and k<=arr[t-1]:
    l=0
    r=t-1
print(l,r)
while l<=r:
    m=(l+r)//2
    if arr[m]==k:
        print("found")
        break
    elif arr[m]<k:
        l=m+1
    else:
        r=m-1
else:
    print("not found")