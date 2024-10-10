arr=[1,2,3,4,5,6,7]
l=0
r=len(arr)-1
while l<r:
    m=(l+r)//2
    if arr[m]==9:
        print("found")
        break
    elif arr[m]<6:
        l=m+1
    else:
        r=m-1
else:
    print("not found")
