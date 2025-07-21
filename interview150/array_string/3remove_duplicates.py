arr=[1,1,2,2,2,3,4]
l=1
for i in range(1,len(arr)):
    if arr[i]!=arr[i-1]:
        arr[l]=arr[i]
        l+=1
print(arr[:l])
    