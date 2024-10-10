arr=[1,2,-1,4,3,5,3]
res=[arr[0],arr[-1]]
# for i in range(1,len(l)-1):
#     if l[i]>l[i-1] and l[i]>l[i+1]:
#         res.append(l[i])
# print(res)

res=[]
def peak(arr,low,high,res):
    if low<=high:
        mid=(low+high)//2
        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==len(arr)-1 or arr[mid+1]<=arr[mid]):
            res.append(arr[mid])
        peak(arr,low,mid-1,res)
        peak(arr,mid+1,high,res)
if len(arr)>2:
    peak(arr,0,len(arr)-1,res)
print(res)