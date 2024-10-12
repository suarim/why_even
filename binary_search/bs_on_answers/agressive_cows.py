arr=[0,3,4,7,9,10]
c=4
def check(arr,c,d):
    no=1
    last=arr[0]
    for i in range(1,len(arr)):
        if arr[i]-last>=d:
            no+=1
            last=arr[i]
    return no>=c
arr.sort()
low=0
high=arr[-1]-arr[0]
ans=-1
while low<=high:
    m=(low+high)//2
    if check(arr,c,m):
        low=m+1
        ans=m
    else:  
        high=m-1
print(ans)