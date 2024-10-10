l=[3,4,13,13,13,20,40,50,50]
k=4
def first(arr,k):
    l=0
    r=len(arr)-1
    res=0
    while l<=r:
        m=(l+r)//2
        if arr[m]==k:
            print("found")
            res=m
            r=m-1
        elif arr[m]<k:
            l=m+1
        else:
            r=m-1
    return res
def last(arr,k):
    l=0
    r=len(arr)-1
    res=0
    while l<=r:
        m=(l+r)//2
        if arr[m]==k:
            print("found")
            res=m
            l=m+1
        elif arr[m]<k:
            l=m+1
        else:
            r=m-1
    return res

print(last(l,k)-first(l,k)+1)