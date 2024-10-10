arr=[1,2,3,4,5,6,7,10,19]
l=0
k=15
r=len(arr)-1
while l<r:
    m=(l+r)//2
    if arr[m]==k:
        print("found")
        break
    elif arr[m]<k:
        l=m+1
    else:
        r=m-1
else:
    print(l)
