arr=[1,2,3,4,5,7,10,19]
l=0
k=22
r=len(arr)-1
while l<=r:
    m=(l+r)//2
    if arr[m]==k:
        print("found")
        break
    elif arr[m]<k:
        l=m+1
    else:
        r=m-1
print(len(arr))
print(l)
if l>=len(arr):
    print(arr[-1],k)
elif l==0:
    print(k,arr[0])
else:
    print(arr[l-1],arr[l])