arr=[1,1,1,1,2,2,3,4,4,4,5]
l=2
for i in range(2,len(arr)):
    if arr[i]!=arr[i-2]:
        arr[l]=arr[i]
        l+=1
print(arr[:l])